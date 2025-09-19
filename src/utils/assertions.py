from typing import Any, Dict, List
import requests
from .logger import logger

class APIAssert:
    """Custom assertions for API testing"""
    
    @staticmethod
    def assert_status_code(response: requests.Response, expected_codes: tuple) -> None:
        """Assert response status code"""
        assert response.status_code in expected_codes, (
            f"Expected status code to be one of {expected_codes}, "
            f"but got {response.status_code}"
        )
    
    @staticmethod
    def assert_json_has_keys(response: requests.Response, keys: List[str]) -> None:
        """Assert JSON response has required keys"""
        body = response.json()
        for key in keys:
            assert key in body, f"Response is missing required key: {key}"
    
    @staticmethod
    def assert_json_value(response: requests.Response, key: str, expected_value: Any) -> None:
        """Assert JSON response has expected value for key"""
        body = response.json()
        assert key in body, f"Response is missing key: {key}"
        assert body[key] == expected_value, (
            f"Expected value '{expected_value}' for key '{key}', "
            f"but got '{body[key]}'"
        )
    
    @staticmethod
    def assert_json_structure(response: requests.Response, expected_structure: Dict[str, type]) -> None:
        """Assert JSON response matches expected structure"""
        body = response.json()
        for key, expected_type in expected_structure.items():
            assert key in body, f"Response is missing key: {key}"
            assert isinstance(body[key], expected_type), (
                f"Expected type {expected_type.__name__} for key '{key}', "
                f"but got {type(body[key]).__name__}"
            )
    
    @staticmethod
    def assert_response_time(response: requests.Response, max_time: float) -> None:
        """Assert response time is within expected limit"""
        assert response.elapsed.total_seconds() <= max_time, (
            f"Response time {response.elapsed.total_seconds()}s "
            f"exceeded maximum {max_time}s"
        )
