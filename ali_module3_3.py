from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    Text: str


@app.post("/message")
def create_message(data: Message):
    return {
        "Text": data.Text
    }