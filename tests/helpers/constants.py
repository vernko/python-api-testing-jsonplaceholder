"""
Constants for API testing.
Contains base URLs, endpoints, and configuration.
"""

# Base URL
BASE_URL = "https://jsonplaceholder.typicode.com"

# Endpoints
ENDPOINTS = {
    "POSTS": "/posts",
    "USERS": "/users",
    "COMMENTS": "/comments",
    "TODOS": "/todos",
}

# Common headers (if needed later)
HEADERS = {
    "Content-Type": "application/json",
}

# Performance thresholds (for later tickets)
MAX_RESPONSE_TIME = 2.0  # seconds
ACCEPTABLE_RESPONSE_TIME = 0.5  # seconds