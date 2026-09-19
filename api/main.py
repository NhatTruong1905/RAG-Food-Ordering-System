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

app = FastAPI(title="RAG Food Ordering API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=False)
