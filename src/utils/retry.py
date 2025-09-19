import time
from functools import wraps
from typing import Callable, Any
from .logger import logger
from .config import config

def retry(func: Callable) -> Callable:
    """Decorator to retry failed API calls"""
    
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        attempts = config.get_config('api.retry_attempts')
        delay = config.get_config('api.retry_delay')
        last_exception = None
        
        for attempt in range(attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                if attempt < attempts - 1:
                    logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
                    time.sleep(delay)
                    continue
                raise last_exception
    
    return wrapper
