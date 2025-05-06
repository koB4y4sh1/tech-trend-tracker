import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv 

from src.api.crawl import router as crawl_router

# .env を読み込む（ローカル開発時のみ有効）
load_dotenv()

app = FastAPI()

# ルーティング設定
app.include_router(crawl_router)

# CORS設定
origins = [
    "http://localhost:3000",
    os.environ.get("WEB_BASE_URL"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# ローカル開発時のみ`py main.py`で起動する
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)