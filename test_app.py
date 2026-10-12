from app import app, add


def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 201
    assert b"Hello" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.get_json() == {"status": "ok"}


def test_add():
    assert add(2, 3) == 5
