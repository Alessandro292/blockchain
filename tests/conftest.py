import pytest

from app_factory import create_app

@pytest.fixture
def app():
    return create_app(config_name='test')

@pytest.fixture
def client(app):
    return app.test_client()



