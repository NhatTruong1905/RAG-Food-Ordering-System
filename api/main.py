import os
import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import uvicorn

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from rag.pipeline import rag

app = FastAPI(title="RAG Food Ordering API", version="1.0.0")

# Cấu hình danh sách domain được phép truy cập (Local & Railway Production)
default_origins = [
    "http://localhost:5000",
    "http://127.0.0.1:5000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://food-ordering-system-production-1cd8.up.railway.app",
]
env_origins = os.getenv("ALLOWED_ORIGINS", "")
custom_origins = [o.strip() for o in env_origins.split(",") if o.strip()]
all_origins = list(set(default_origins + custom_origins))

app.add_middleware(
    CORSMiddleware,
    allow_origins=all_origins if env_origins != "*" else ["*"],
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1|.*\.railway\.app)(:\d+)?$",
    allow_credentials=True if env_origins != "*" else False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "status": "online",
        "service": "RAG Food Ordering API",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/query/stream")
def query_stream_post(payload: dict):
    question = payload.get("query", "")
    top_k = payload.get("top_k", 3)
    sse = payload.get("sse", False)
    if not question:
        return {"error": "Vui lòng cung cấp query"}

    media_type = "text/event-stream" if sse else "text/plain; charset=utf-8"
    return StreamingResponse(
        rag.query_stream(user_query=question, top_k=top_k, sse=sse),
        media_type=media_type
    )


@app.get("/query/stream")
def query_stream_get(query: str, top_k: int = 3, sse: bool = False):
    if not query:
        return {"error": "Vui lòng cung cấp query"}

    media_type = "text/event-stream" if sse else "text/plain; charset=utf-8"
    return StreamingResponse(
        rag.query_stream(user_query=query, top_k=top_k, sse=sse),
        media_type=media_type
    )


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("api.main:app", host=host, port=port, reload=False)
