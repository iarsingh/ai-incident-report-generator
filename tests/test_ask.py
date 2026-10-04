from fastapi.testclient import TestClient
from irgen.main import app

client = TestClient(app)


def test_answers_and_refuses():
    hit = client.post("/ask", json={"question": 'Who may roll back when the error rate doubles?'}).json()
    assert hit["answered"] is True
    assert hit["citation"] == "rollback"
    miss = client.post("/ask", json={"question": 'cafeteria soup'}).json()
    assert miss["answered"] is False


def test_empty_is_refused():
    assert client.post("/ask", json={"question": " "}).status_code == 422
