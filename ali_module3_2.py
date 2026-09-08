from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Message(BaseModel):
    message: str


@app.post("/message")
def create_message(data: Message):
    return {
        "message": data.message,
        "timestamp": datetime.now()
    }