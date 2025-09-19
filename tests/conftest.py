import pytest
import os
from src.api_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    base = os.getenv("BOOKS_API_BASE", "https://fakerestapi.azurewebsites.net")
    return APIClient(base_url=base)

@pytest.fixture
def sample_book():
    here = os.path.join(os.path.dirname(__file__), "data", "sample_book.json")
    import json
    with open(here, "r", encoding="utf-8") as f:
        book = json.load(f)
    book_to_send = {k: v for k, v in book.items() if k != "id"}
    return book_to_send