import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    # Check for key HTML content
    assert b"Jarvis - GitHub Actions" in response.data
    assert b"Hello, Ashish Singh" in response.data
    assert b"Connect with me" in response.data
    assert b"GitHub" in response.data
    assert b"LinkedIn" in response.data
    assert b"Portfolio" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "message": "Service is healthy"}
