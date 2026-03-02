from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Assalamu Aleikum!"}

def test_sum():
    response = client.get("/sum?a=5&b=7")
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_multiplay():
    response = client.get("/multiplay?a=5&b=6")
    assert response.status_code == 200
    assert response.json() == {"result": 30}