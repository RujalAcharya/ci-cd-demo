from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == 5
    
    response = client.post("/subtract", json={'a': 3, 'b': 2})
    assert response.status_code == 200
    assert response.json()["result"] == 1
