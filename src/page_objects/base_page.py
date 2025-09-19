import requests
import logging
from src.interfaces import APIClientInterface, ResponseValidator

logger = logging.getLogger(__name__)

class BaseValidator(ResponseValidator):
    """Basic implementation of response validation"""
    
    def validate_status(self, response: requests.Response, expected_status: tuple = (200,)) -> None:
        """Validate response status code"""
        if response.status_code not in expected_status:
            logger.error(f"Got status code {response.status_code}, expected {expected_status}")
            logger.error(f"Response body: {response.text}")
        assert response.status_code in expected_status, \
            f"Expected status {expected_status}, got {response.status_code}"
    
    def validate_json_fields(self, data: dict, required_fields: list) -> None:
        """Validate required fields in JSON response"""
        missing = [field for field in required_fields if field not in data]
        if missing:
            logger.error(f"Missing required fields: {missing}")
            assert not missing, f"Missing required fields: {missing}"

class BasePage:
    """Base page object that all other page objects will inherit from"""
    
    def __init__(self, api_client: APIClientInterface):
        """Initialize with API client and validator"""
        self.api_client = api_client
        self.validator = BaseValidator()
    
    def _validate_response(self, response: requests.Response, expected_status: tuple = (200,)) -> None:
        """Validate API response"""
        self.validator.validate_status(response, expected_status)
    
    def _validate_fields(self, data: dict, required_fields: list) -> None:
        """Validate response data fields"""
        self.validator.validate_json_fields(data, required_fields)
