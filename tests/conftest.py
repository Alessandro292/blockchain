import pytest

from app.instances.blockchain import Blockchain
from app.app_factory import create_app

@pytest.fixture
def app():
    return create_app(config_name='test')

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def blockchain():
    return Blockchain()

