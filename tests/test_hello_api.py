
from app.config.constants import API_PREFIX

def test_hello_world_endpoint(client):
    response = client.get(f'{API_PREFIX}/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_hello_route_without_name(client):
    response = client.get(f'{API_PREFIX}/hello/')
    assert response.status_code == 200
    assert b'Hello World, from Flask' in response.data

def test_hello_route_with_name(client):
    response = client.get(f'{API_PREFIX}/hello/John')
    assert response.status_code == 200
    assert b'Hello John, from Flask' in response.data



