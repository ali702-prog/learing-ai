from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def say_hello(name: str = "World"):
  return {"message": f"Hello {name}"}
