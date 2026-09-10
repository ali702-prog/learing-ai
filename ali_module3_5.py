from fastapi import FastAPI
from pydantic import BaseModel
import random
import logging

app = FastAPI()


# -------------------------
# LOGGING
# -------------------------

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

# Log to console
console_handler = logging.StreamHandler()

# Log to file
file_handler = logging.FileHandler("my_file.log")

# Log format
formatter = logging.Formatter(
    "%(asctime)s - %(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


# -------------------------
# MIDDLEWARE
# -------------------------

@app.middleware("http")
async def log_requests(request, call_next):

    response = await call_next(request)

    logger.info(
        f"Method: {request.method} | "
        f"Path: {request.url.path} | "
        f"Status: {response.status_code}"
    )

    return response


# -------------------------
# PERSON API
# -------------------------

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