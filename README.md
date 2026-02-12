# Python API Testing - JSONPlaceholder

![API Tests](https://github.com/vernko/python-api-testing-jsonplaceholder/actions/workflows/api-tests.yml/badge.svg)

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

## CI/CD

This project uses GitHub Actions for continuous integration. Tests run automatically on:
- Every push to `main` branch
- Every pull request to `main` branch

### Workflow Details

The CI pipeline:
1. Sets up Python 3.9 environment
2. Installs `uv` package manager
3. Installs project dependencies
4. Runs all tests with pytest
5. Uploads test results as artifacts on failure

See `.github/workflows/api-tests.yml` for full workflow configuration.

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