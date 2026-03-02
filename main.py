from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Assalamu Aleikum!"}

@app.get("/sum/")
def get_sum(a: int, b: int):
    return {"result": a + b}

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/divide/")
def get_divide(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}