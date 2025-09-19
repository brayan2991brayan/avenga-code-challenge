import json
import os
from typing import Dict, Any

class TestData:
    """Test data provider for the automation framework"""
    
    @staticmethod
    def load_test_data(file_name: str) -> Dict[str, Any]:
        """Load test data from JSON file"""
        data_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'tests',
            'data',
            file_name
        )
        with open(data_path, 'r') as f:
            return json.load(f)
            
    @staticmethod
    def get_sample_book() -> Dict[str, Any]:
        """Get sample book data"""
        return {
            "id": 0,  # Will be assigned by the API
            "title": "Sample Book",
            "description": "A sample book for testing",
            "pageCount": 100,
            "excerpt": "Sample excerpt",
            "publishDate": "2023-09-19T00:00:00Z"
        }
        
    @staticmethod
    def get_invalid_book() -> Dict[str, Any]:
        """Get invalid book data for negative testing"""
        return {
            "title": "",  # Invalid empty title
            "pageCount": -1,  # Invalid negative page count
        }
