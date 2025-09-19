import logging
import os
from datetime import datetime

class Logger:
    """Custom logger for test automation framework"""
    
    def __init__(self):
        self.logger = logging.getLogger('api_automation')
        if not self.logger.handlers:
            self.setup_logger()
    
    def setup_logger(self):
        """Setup logger with file and console handlers"""
        self.logger.setLevel(logging.INFO)
        
        # Create logs directory if it doesn't exist
        logs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
        os.makedirs(logs_dir, exist_ok=True)
        
        # File handler
        log_file = os.path.join(logs_dir, f'test_run_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message: str):
        """Log info level message"""
        self.logger.info(message)
    
    def error(self, message: str):
        """Log error level message"""
        self.logger.error(message)
    
    def debug(self, message: str):
        """Log debug level message"""
        self.logger.debug(message)

logger = Logger()
