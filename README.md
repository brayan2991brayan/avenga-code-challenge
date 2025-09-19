# Books API Test Automation Framework 📚

This project is a test automation framework for the Books API, built using Python and following best practices such as Page Object Model (POM) and SOLID principles.

## 🎯 Target API
- Base URL: `https://fakerestapi.azurewebsites.net`
- Endpoints: 
  - 📖 `/api/v1/Books` - Books collection
  - 📕 `/api/v1/Books/{id}` - Individual book

## 🏗️ Project Structure

```
├── config/
│   └── dev.json           # Environment configuration
├── logs/                  # Test execution logs
├── reports/              # HTML test reports
├── src/
│   ├── api_client.py     # API client implementation
│   ├── interfaces.py     # Abstract interfaces
│   ├── page_objects/     # Page Object Model implementations
│   │   ├── base_page.py  # Base page with common functionality
│   │   └── books_page.py # Books-specific page object
│   └── utils/           # Utility modules
│       ├── assertions.py # Custom test assertions
│       ├── config.py     # Configuration management
│       ├── logger.py     # Logging setup
│       ├── retry.py      # Retry mechanism
│       └── test_data.py  # Test data helpers
└── tests/
    ├── conftest.py       # pytest fixtures
    └── test_books_api.py # API test cases
```

## ✨ Features

- ♻️ Page Object Model design pattern
- 🎯 SOLID principles implementation
- 📝 Detailed HTML test reports
- 🔄 Automatic retry mechanism for flaky tests
- 📊 Comprehensive logging
- ⚙️ Environment-based configuration
- 🧪 Data-driven test approach

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- virtualenv (recommended)

### 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd avenga-code-challenge
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Running Tests

### Run all tests:
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run specific test file:
```bash
pytest tests/test_books_api.py -v
```

### Run smoke tests:
```bash
pytest -m smoke -v
```

## 📊 Test Reports

After test execution, HTML reports are generated in the `reports/` directory. Open `reports/report.html` in a web browser to view detailed test results.

## 🛠️ Development Guidelines

### Adding New Tests

1. Create page objects in `src/page_objects/` for new API endpoints
2. Implement test cases in `tests/` directory
3. Use fixtures from `conftest.py` for common setup
4. Follow existing patterns for consistency

### Best Practices

- ✅ Use type hints for better code maintainability
- ✅ Follow PEP 8 style guide
- ✅ Write descriptive docstrings
- ✅ Implement proper error handling
- ✅ Keep test cases independent
- ✅ Use appropriate markers for test categories

## 📝 Documentation

- Page Objects: Each page object represents an API endpoint and encapsulates all operations and validations
- Fixtures: Common test fixtures are available in `conftest.py`
- Configuration: Environment settings in `config/dev.json`
- Logging: Test execution logs are stored in `logs/` directory

## 🔍 Code Quality

The project maintains high code quality standards through:

- Type hints
- Comprehensive documentation
- SOLID principles
- Clean code practices
- Proper error handling
- Consistent naming conventions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ✨ Acknowledgments

- Thanks to Avenga for the code challenge opportunity
- Built with Python and pytest
- Inspired by best practices in test automation

---
Made with ❤️ for Avenga Code Challenge
