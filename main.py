from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Assalamu Aleikum!"}

@app.get("/sum/{a}/{b}")
def get_sum(a: int, b: int):
    return {"result": a + b}