from setuptools import setup, find_packages

setup(
    name="avenga-api-test",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.25.0",
        "pytest>=6.0.0",
        "pytest-html>=3.1.1"
    ]
)
