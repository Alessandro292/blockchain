
from app.config.constants import API_PREFIX

def test_hello_world_endpoint(client):
    response = client.get(f'{API_PREFIX}/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
