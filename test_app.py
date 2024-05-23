import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_create_user(client):
    response = client.post('/users', json={"name": "Krzysztof", "lastname": "Skórczewski"})
    assert response.status_code == 201
    assert response.json["name"] == "Krzysztof"
    assert response.json["lastname"] == "Skórczewski"

def test_update_user(client):
    response = client.patch('/users/1', json={"name": "Updated Name"})
    assert response.status_code == 204

def test_replace_user(client):
    response = client.put('/users/1', json={"name": "New Name", "lastname": "New Lastname"})
    assert response.status_code == 204

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == 204
