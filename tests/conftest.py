import pytest
from utils.request_manager import RequestManager

@pytest.fixture(scope="session")
def request_manager():
    """Fixture to provide a RequestManager instance."""
    return RequestManager()
