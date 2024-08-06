from fastapi import FastAPI
from fastapi.params import Body
import pydantic

app = FastAPI()

@app.get("/")
def root():
    return {"data": "This is a placeholder!!!"}

@app.post("/postdata")
def post_data(payload: dict = Body(...)):
    print(payload)
    return {"new post": f"Title: {payload['title']}, Content: {payload['content']}"}
