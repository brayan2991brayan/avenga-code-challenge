import os
import json
from typing import Any, Dict

class ConfigManager:
    """Configuration manager for test automation framework"""
    
    def __init__(self):
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file based on environment"""
        env = os.getenv('TEST_ENV', 'dev')
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'config',
            f'{env}.json'
        )
        
        if not os.path.exists(config_path):
            return {
                'api': {
                    'base_url': os.getenv('BOOKS_API_BASE', 'https://fakerestapi.azurewebsites.net'),
                    'timeout': int(os.getenv('API_TIMEOUT', '10')),
                    'retry_attempts': int(os.getenv('RETRY_ATTEMPTS', '3')),
                    'retry_delay': int(os.getenv('RETRY_DELAY', '1'))
                }
            }
            
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def get_config(self, key: str = None) -> Any:
        """Get configuration value by key"""
        if key is None:
            return self.config
        
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k)
            if value is None:
                return None
        return value

config = ConfigManager()
