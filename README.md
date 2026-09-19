# 🍜 Project RAG Food Ordering System (LangChain, FAISS & Streaming API)

Hệ thống RAG xây dựng hoàn toàn bằng **LangChain**, trích xuất thông tin từ file SQL thành tài liệu Markdown trong `papers/`, cắt theo từng đoạn (`\n\n`) bằng `CharacterTextSplitter`, lưu trữ chỉ mục trong **FAISS Vector Database** (`rag/vector_db/`), và cung cấp API hỗ trợ cả **JSON thông thường** và **Streaming thời gian thực (Real-time Stream)** tại `api/main.py`.

---

## 📁 Cấu Trúc Dự Án

```text
RAG-Food-Ordering-System/
├── api/
│   ├── __init__.py
│   └── main.py                         # FastAPI server (hỗ trợ /query, /query/stream, /health)
├── papers/
│   └── food_ordering_knowledge_base.md # File markdown tài liệu trích từ SQL
├── rag/
│   ├── __init__.py
│   ├── pipeline.py                     # Pipeline LangChain: Loader, Splitter, FAISS, Query & Streaming
│   └── vector_db/                      # FAISS Vector Database lưu sẵn theo chuẩn LangChain
│       ├── index.faiss                 # File nhị phân chỉ mục vector FAISS
│       ├── index.pkl                   # Metadata lưu trữ các Document LangChain
│       └── embeddings.pkl              # Trọng số mô hình embedding
├── food_ordering_db.sql                # File database gốc
├── requirements.txt                    # Thư viện phụ thuộc
└── README.md                           # Hướng dẫn sử dụng
```

---

## 🚀 Khởi Động Server

```bash
python api/main.py
```
Server chạy tại `http://127.0.0.1:8000`.

---

## 📡 Các Endpoint API

### 1. Truy Vấn Dạng Stream (`POST /query/stream` hoặc `GET /query/stream`)
Truy vấn trả về kết quả theo thời gian thực (Real-time Stream / Typewriter effect), thích hợp cho giao diện Chatbot, Web và Mobile.

#### A. Gọi Bằng cURL (Xem stream chạy trực tiếp trên terminal):
```bash
curl -N -X POST "http://127.0.0.1:8000/query/stream" \
  -H "Content-Type: application/json" \
  -d '{"query": "Địa chỉ quán Pizza 4Ps và món đặc sắc?", "top_k": 2}'
```

#### B. Gọi Bằng JavaScript / Frontend (Fetch Stream):
```javascript
const response = await fetch("http://127.0.0.1:8000/query/stream", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ query: "Quán nào có món phở bò tái lăn?", top_k: 2 })
});

const reader = response.body.getReader();
const decoder = new TextDecoder();

while (true) {
  const { value, done } = await reader.read();
  if (done) break;
  const chunk = decoder.decode(value);
  process.stdout.write(chunk); // Hiển thị từng token/từ tới người dùng
}
```

#### C. Gọi Bằng Python (`requests` với `stream=True`):
```python
import requests

url = "http://127.0.0.1:8000/query/stream"
payload = {"query": "Món bánh xèo tôm nhảy ở đâu?", "top_k": 1}

with requests.post(url, json=payload, stream=True) as response:
    for chunk in response.iter_content(chunk_size=None, decode_unicode=True):
        print(chunk, end="", flush=True)
```

#### D. Chuẩn Server-Sent Events (SSE) cho EventSource:
Thêm `"sse": true` trong body hoặc param:
```bash
curl -N "http://127.0.0.1:8000/query/stream?query=Pizza&sse=true"
```
Kết quả trả về từng dòng theo định dạng SSE:
```text
data: {"text": "🔍 Kết quả trích xuất từ papers..."}
...
data: [DONE]
```

---

### 2. Truy Vấn Dạng JSON Thông Thường (`POST /query`)
Dành cho trường hợp muốn nhận toàn bộ kết quả một lần:
```bash
curl -X POST "http://127.0.0.1:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "Quán nào có món phở bò tái lăn?", "top_k": 2}'
```