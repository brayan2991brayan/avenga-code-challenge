from abc import ABC, abstractmethod
from typing import Protocol
import requests

class APIClientInterface(Protocol):
    """Interface for API clients"""
    def get_books(self) -> requests.Response:
        """Get all books"""
        ...
    
    def get_book(self, book_id: int) -> requests.Response:
        """Get a specific book"""
        ...
    
    def create_book(self, book_data: dict) -> requests.Response:
        """Create a new book"""
        ...
    
    def update_book(self, book_id: int, book_data: dict) -> requests.Response:
        """Update a book"""
        ...
    
    def delete_book(self, book_id: int) -> requests.Response:
        """Delete a book"""
        ...

class ResponseValidator(ABC):
    """Interface for response validation"""
    @abstractmethod
    def validate_status(self, response: requests.Response, expected_status: tuple) -> None:
        """Validate response status code"""
        pass
    
    @abstractmethod
    def validate_json_fields(self, data: dict, required_fields: list) -> None:
        """Validate JSON response fields"""
        pass
