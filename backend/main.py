from typing import Union
from pydantic import BaseModel

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return "ConversAI Backend Testing."


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/healthy")
async def healthy():
    return "Healthy"
    

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
