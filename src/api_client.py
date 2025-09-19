# src/api_client.py
from typing import Any, Dict, Optional
import os
import requests

class APIClient:
    """
    Simple API client for FakeRestAPI Books endpoints.
    Uses a requests.Session to keep connection pooling and sane defaults.
    """
    def __init__(self, base_url: Optional[str] = None, timeout: int = 10):
        self.base_url = base_url or os.getenv("BOOKS_API_BASE", "https://fakerestapi.azurewebsites.net")
        self.session = requests.Session()
        self.timeout = timeout
        # Default headers - can be extended
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def _url(self, path: str) -> str:
        return f"{self.base_url.rstrip('/')}{path}"

    def get_books(self) -> requests.Response:
        return self.session.get(self._url("/api/v1/Books"), timeout=self.timeout)

    def get_book(self, book_id: int) -> requests.Response:
        return self.session.get(self._url(f"/api/v1/Books/{book_id}"), timeout=self.timeout)

    def create_book(self, payload: Dict[str, Any]) -> requests.Response:
        return self.session.post(self._url("/api/v1/Books"), json=payload, timeout=self.timeout)

    def update_book(self, book_id: int, payload: Dict[str, Any]) -> requests.Response:
        return self.session.put(self._url(f"/api/v1/Books/{book_id}"), json=payload, timeout=self.timeout)

    def delete_book(self, book_id: int) -> requests.Response:
        return self.session.delete(self._url(f"/api/v1/Books/{book_id}"), timeout=self.timeout)