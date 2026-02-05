# Python API Testing - JSONPlaceholder

REST API test automation suite using Python, pytest, and requests library. Tests the JSONPlaceholder fake REST API to demonstrate API testing skills.

## Setup
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

## Run Tests
```bash
# Run all tests
uv run pytest -v

# Run specific test file
uv run pytest tests/test_posts.py -v
```

## Project Structure
```
tests/
├── helpers/          # Helper functions and utilities
└── test_posts.py    # Tests for /posts endpoint
```

## Technologies

- Python 3.9+
- pytest
- requests