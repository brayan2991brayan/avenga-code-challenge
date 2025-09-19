# src/api_client.py
import requests
from src.interfaces import APIClientInterface

class APIClient(APIClientInterface):
    """Implementation of the API client interface for Books REST API"""
    
    def __init__(self, base_url: str = "https://fakerestapi.azurewebsites.net"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def _url(self, path: str) -> str:
        """Build full URL for API endpoint"""
        return f"{self.base_url.rstrip('/')}{path}"

    def get_books(self):
        """Get all books"""
        return self.session.get(self._url("/api/v1/Books"))

    def get_book(self, book_id: int):
        """Get a specific book by ID"""
        return self.session.get(self._url(f"/api/v1/Books/{book_id}"))

    def create_book(self, book_data: dict) -> requests.Response:
        """Create a new book"""
        response = self.session.post(self._url("/api/v1/Books"), json=book_data)
        print(f"API Create Book Response: {response.status_code}")
        print(f"Response Content: {response.text}")
        return response

    def update_book(self, book_id: int, book_data: dict) -> requests.Response:
        """Update an existing book"""
        return self.session.put(self._url(f"/api/v1/Books/{book_id}"), json=book_data)

    def delete_book(self, book_id: int) -> requests.Response:
        """Delete a book"""
        return self.session.delete(self._url(f"/api/v1/Books/{book_id}"))