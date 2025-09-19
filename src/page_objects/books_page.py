from dataclasses import dataclass
from typing import Optional, List, Dict, Any
import requests
from src.page_objects.base_page import BasePage

@dataclass
class BookData:
    """Data class for book information"""
    id: int = 0
    title: str = ""
    description: str = ""
    page_count: int = 0
    excerpt: str = ""
    publish_date: str = ""

    @classmethod
    def from_response(cls, data: dict) -> 'BookData':
        """Create BookData from API response"""
        if not isinstance(data, dict):
            raise ValueError("Response data must be a dictionary")

        book = cls(
            id=int(data.get('id', 0)),  # Ensure id is an integer
            title=str(data.get('title', '')),
            description=str(data.get('description', '')),
            page_count=int(data.get('pageCount', 0)),
            excerpt=str(data.get('excerpt', '')),
            publish_date=str(data.get('publishDate', ''))
        )

        return book

    def to_dict(self) -> dict:
        """Convert to dictionary for API requests"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'pageCount': self.page_count,
            'excerpt': self.excerpt,
            'publishDate': self.publish_date
        }

class BooksPage(BasePage):
    """Handles all books-related API operations"""
    
    REQUIRED_FIELDS = ['id', 'title']
    
    def get_all_books(self) -> List[BookData]:
        """Get all books from the API"""
        response = self.api_client.get_books()
        self._validate_response(response)
        return [BookData.from_response(book) for book in response.json()]

    def get_book_by_id(self, book_id: int, expect_found: bool = True) -> Optional[BookData]:
        """Get a specific book by ID"""
        response = self.api_client.get_book(book_id)
        expected_codes = (200,) if expect_found else (200, 404)
        self._validate_response(response, expected_codes)
        
        if response.status_code == 200 and expect_found:
            data = response.json()
            self._validate_fields(data, self.REQUIRED_FIELDS)
            return BookData.from_response(data)
        return None
        
    def create_book(self, book_data: BookData) -> BookData:
        """Create a new book"""
        if not book_data.title:
            raise ValueError("Book title cannot be empty")

        response = self.api_client.create_book(book_data.to_dict())
        self._validate_response(response, (200, 201))
        
        response_data = response.json()
        if not isinstance(response_data, dict):
            raise ValueError(f"Invalid API response format: {response_data}")
            
        return BookData.from_response(response_data)
        
    def update_book(self, book_id: int, book_data: BookData) -> Optional[BookData]:
        """Update an existing book"""
        if not book_data.title:
            raise AssertionError("Book title cannot be empty")
            
        response = self.api_client.update_book(book_id, book_data.to_dict())
        self._validate_response(response, (200, 201, 204))
        
        if response.status_code in (200, 201):
            return BookData.from_response(response.json())
        return None
        
    def delete_book(self, book_id: int) -> None:
        """Delete a book"""
        response = self.api_client.delete_book(book_id)
        self._validate_response(response, (200, 204))


