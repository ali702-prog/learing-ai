from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

saved_person = {}


class Person(BaseModel):
    name: str
    phone_number: str


@app.post("/person")
def create_person(person: Person):
    saved_person["name"] = person.name
    saved_person["phone_number"] = person.phone_number

    return saved_person


@app.get("/person")
def read_person():
    random_number = random.randint(1, 100)

    return {
        "name": saved_person["name"],
        "phone_number": saved_person["phone_number"],
        "random_number": random_number
    }