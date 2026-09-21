import os
import sys
import json
import time
import pickle
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from dotenv import load_dotenv

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from langchain_core.embeddings import Embeddings
from langchain_core.documents import Document
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS  
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

BASE_DIR = Path(__file__).resolve().parent.parent
PAPERS_DIR = BASE_DIR / "papers"
VECTOR_DB_DIR = BASE_DIR / "rag" / "vector_db"

load_dotenv(BASE_DIR / ".env")
load_dotenv(BASE_DIR / "rag" / ".env")

def strip_markdown(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r'(?m)^#+\s*', '', text)
    text = text.replace('**', '').replace('*', '')
    text = re.sub(r'(?m)^---+', '', text)
    text = text.replace('`', '')
    text = text.replace('__', '')
    return text.strip()

class LangChainLocalEmbeddings(Embeddings):
    def __init__(self, max_features: int = 512):
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=max_features, sublinear_tf=True)
        self._fitted = False

    def fit(self, texts: List[str]):
        self.vectorizer.fit(texts)
        self._fitted = True

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        if not self._fitted:
            self.fit(texts)
        vecs = self.vectorizer.transform(texts).toarray().astype(np.float32)
        norms = np.linalg.norm(vecs, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        return (vecs / norms).tolist()

    def embed_query(self, text: str) -> List[float]:
        if not self._fitted:
            raise ValueError("Embeddings chưa được fit với dữ liệu tài liệu!")
        vec = self.vectorizer.transform([text]).toarray().astype(np.float32)[0]
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm
        return vec.tolist()

    def save(self, path: Path):
        with open(path, "wb") as f:
            pickle.dump({"vectorizer": self.vectorizer, "fitted": self._fitted}, f)

    def load(self, path: Path):
        with open(path, "rb") as f:
            data = pickle.load(f)
            self.vectorizer = data["vectorizer"]
            self._fitted = data["fitted"]

class LangChainRAGPipeline:
    def __init__(self, papers_dir: Path = PAPERS_DIR, db_dir: Path = VECTOR_DB_DIR):
        self.papers_dir = Path(papers_dir)
        self.db_dir = Path(db_dir)
        self.db_dir.mkdir(parents=True, exist_ok=True)

        self.api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        self.llm = None

        if self.api_key:
            self.embeddings = GoogleGenerativeAIEmbeddings(
                model="gemini-embedding-001",
                google_api_key=self.api_key
            )
            self.emb_type = "gemini"
        else:
            self.embeddings = LangChainLocalEmbeddings()
            self.emb_type = "local"

        self.vectorstore: Optional[FAISS] = None
        self.retriever = None
        self.rag_chain = None

        self.load_or_build()

    def load_and_split_documents(self) -> List[Document]:
        loader = DirectoryLoader(
            path=str(self.papers_dir),
            glob="*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        raw_docs = loader.load()

        text_splitter = CharacterTextSplitter(
            separator="\n\n",
            chunk_size=600,
            chunk_overlap=50,
            strip_whitespace=True
        )
        splits = text_splitter.split_documents(raw_docs)

        valid_chunks = [
            d for d in splits
            if len(d.page_content.strip()) > 30 and d.page_content.strip() != "---"
        ]
        return valid_chunks

    def build_vector_store(self):
        chunks = self.load_and_split_documents()
        if not chunks:
            return

        if isinstance(self.embeddings, LangChainLocalEmbeddings):
            texts = [c.page_content for c in chunks]
            self.embeddings.fit(texts)
            self.embeddings.save(self.db_dir / "embeddings.pkl")

        self.vectorstore = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

        self.vectorstore.save_local(str(self.db_dir))
        with open(self.db_dir / "emb_type.txt", "w", encoding="utf-8") as f:
            f.write(self.emb_type)

        self._init_chain()

    def load_or_build(self):
        index_file = self.db_dir / "index.faiss"
        pkl_file = self.db_dir / "index.pkl"
        emb_type_file = self.db_dir / "emb_type.txt"

        saved_emb_type = ""
        if emb_type_file.exists():
            with open(emb_type_file, "r", encoding="utf-8") as f:
                saved_emb_type = f.read().strip()

        if index_file.exists() and pkl_file.exists() and (saved_emb_type == self.emb_type):
            try:
                if isinstance(self.embeddings, LangChainLocalEmbeddings):
                    self.embeddings.load(self.db_dir / "embeddings.pkl")

                self.vectorstore = FAISS.load_local(
                    folder_path=str(self.db_dir),
                    embeddings=self.embeddings,
                    allow_dangerous_deserialization=True
                )
                self._init_chain()
                return
            except Exception:
                pass

        self.build_vector_store()

    def _init_chain(self):
        if self.vectorstore is not None:
            self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})

            template = (
                "Bạn là nhân viên tư vấn ẩm thực thân thiện, chu đáo và nhiệt tình của hệ thống Food Ordering System.\n"
                "Thông tin tham khảo:\n\n"
                "{context}\n\n"
                "Tin nhắn của khách hàng: {question}\n\n"
                "QUY TẮC PHẢN HỒI:\n"
                "- XƯNG HÔ VÀ THÁI ĐỘ: Luôn giữ giọng điệu niềm nở, lễ phép, gần gũi và ấm áp. Xưng là 'em' và gọi khách hàng là 'anh/chị'. Khi khách hàng gửi lời chào (như 'xin chào', 'hello', 'hi', 'chào em',...), hãy chào lại vui vẻ và hỏi nhu cầu của anh/chị.\n"
                "- NỘI DUNG TẬP TRUNG Ý CHÍNH: Trả lời thẳng vào trọng tâm câu hỏi. Tuyệt đối KHÔNG nhắc đến các từ ngữ như 'theo tài liệu', 'trích xuất từ papers', 'theo dữ liệu đã cho' hoặc nói mình lấy thông tin ở đâu. Hãy tư vấn tự nhiên như bạn đã nắm rõ thực đơn.\n"
                "- THÔNG TIN CẦN NÊU: Nêu ngắn gọn, rõ ràng các ý chính gồm tên món, giá tiền (VNĐ), tên quán hoặc địa chỉ để anh/chị dễ chọn món nhanh nhất, không viết lan man dài dòng.\n"
                "- ĐỊNH DẠNG VĂN BẢN THUẦN (PLAIN TEXT): Tuyệt đối KHÔNG sử dụng các ký tự định dạng Markdown như dấu sao (** in đậm, * in nghiêng), dấu thăng (#, ##, ### tiêu đề), dấu gạch dưới (_), dấu tick ngược (` hoặc ```). Xuống dòng rõ ràng, dùng số thứ tự thông thường (1., 2.) hoặc dấu gạch đầu dòng ngắn gọn để phân tách ý."
            )
            self.prompt = ChatPromptTemplate.from_template(template)

            def format_docs(docs: List[Document]) -> str:
                return "\n\n---\n\n".join(doc.page_content for doc in docs)
            self._format_docs = format_docs

            if self.api_key:
                try:
                    self.llm = ChatGoogleGenerativeAI(
                        model="gemini-flash-lite-latest",
                        google_api_key=self.api_key,
                        temperature=0.2
                    )
                except Exception:
                    self.llm = None
            else:
                self.llm = None

            if self.llm:
                self.rag_chain = (
                    {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
                    | self.prompt
                    | self.llm
                    | StrOutputParser()
                )
            else:
                self.rag_chain = (
                    {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
                    | RunnableLambda(lambda x: strip_markdown(x["context"]))
                )

    @property
    def index(self):
        return self.vectorstore.index if self.vectorstore else None

    def query_stream(self, user_query: str, top_k: int = 3, sse: bool = False):
        if self.vectorstore is None or self.retriever is None:
            msg = "FAISS vectorstore chưa được khởi tạo."
            yield f"data: {json.dumps({'text': msg}, ensure_ascii=False)}\n\n" if sse else msg
            if sse:
                yield "data: [DONE]\n\n"
            return

        retriever = self.vectorstore.as_retriever(search_kwargs={"k": top_k})

        if self.llm and self.rag_chain:
            try:
                chain = self.rag_chain
                if top_k != 3:
                    chain = (
                        {"context": retriever | self._format_docs, "question": RunnablePassthrough()}
                        | self.prompt
                        | self.llm
                        | StrOutputParser()
                    )
                for chunk in chain.stream(user_query):
                    if chunk:
                        yield f"data: {json.dumps({'text': chunk}, ensure_ascii=False)}\n\n" if sse else chunk
                if sse:
                    yield "data: [DONE]\n\n"
                return
            except Exception:
                pass

        matched_docs = retriever.invoke(user_query)
        if not matched_docs:
            msg = "Không tìm thấy thông tin phù hợp trong kho tài liệu."
            yield f"data: {json.dumps({'text': msg}, ensure_ascii=False)}\n\n" if sse else msg
            if sse:
                yield "data: [DONE]\n\n"
            return

        header = f"Dạ em gửi anh/chị thông tin về \"{user_query}\":\n\n"
        yield f"data: {json.dumps({'text': header}, ensure_ascii=False)}\n\n" if sse else header

        best_doc = matched_docs[0]
        text = strip_markdown(best_doc.page_content)
        words = text.split(" ")
        buffer = []
        for word in words:
            buffer.append(word)
            if len(buffer) >= 3:
                chunk = " ".join(buffer) + " "
                yield f"data: {json.dumps({'text': chunk}, ensure_ascii=False)}\n\n" if sse else chunk
                buffer = []
                time.sleep(0.012)

        if buffer:
            chunk = " ".join(buffer) + "\n"
            yield f"data: {json.dumps({'text': chunk}, ensure_ascii=False)}\n\n" if sse else chunk

        closing = "\nAnh/chị cần em hỗ trợ thêm gì cứ nhắn em nhé ạ!\n"
        yield f"data: {json.dumps({'text': closing}, ensure_ascii=False)}\n\n" if sse else closing

        if sse:
            yield "data: [DONE]\n\n"

rag = LangChainRAGPipeline()
