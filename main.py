from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Assalamu Aleikum!"}

@app.get("/sum/")
def get_sum(a: int, b: int):
    return {"result": a + b}

@app.get("/multiplay/")
def get_multiplay(a: int, b: int):
    return {"result": a * b}