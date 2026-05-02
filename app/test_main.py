from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_conversion():
    response = client.post("/", data={
        "amount": 43.95, 
        "from_curr": "UAH", 
        "to_curr": "USD"
    })
    
    assert response.status_code == 200
    assert "1.0" in response.text