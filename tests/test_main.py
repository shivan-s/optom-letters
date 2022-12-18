"""Main testing."""

from fastapi import FastAPI
from fastapi.testclient import TestClient

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200

def test_generate_letter():
    response = client.post("/generate_letter", data={})
    assert response.statuc_code = 200
