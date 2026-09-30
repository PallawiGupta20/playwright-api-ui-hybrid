import pytest
from api.api_client import ApiClient


@pytest.fixture
def api_client(playwright):
    request_context = playwright.request.new_context()
    client = ApiClient(request_context)
    yield client
    request_context.dispose()
