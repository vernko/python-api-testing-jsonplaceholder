"""
Helper functions for API testing.
"""

import requests
from tests.helpers.constants import BASE_URL

def make_request(method, endpoint, **kwargs):
    """
    Make an API request.
    
    Args:
        method: HTTP method (GET, POST, PUT, DELETE)
        endpoint: API endpoint path
        **kwargs: Additional arguments to pass to requests
    
    Returns:
        Response object
    """
    url = f"{BASE_URL}{endpoint}"
    response = requests.request(method, url, **kwargs)
    return response

def validate_status_code(response, expected_code):
    """
    Validate response status code.
    
    Args:
        response: Response object from requests
        expected_code: Expected HTTP status code (e.g., 200, 201, 404)
    
    Raises:
        AssertionError: If status code doesn't match expected
    """
    assert response.status_code == expected_code, (
        f"Expected status code {expected_code}, got {response.status_code}. "
        f"Response: {response.text}"
    )

def assert_response_time(response, max_time):
    """
    Assert that response time is within acceptable limit.
    
    Args:
        response: Response object from requests
        max_time: Maximum acceptable response time in seconds
    
    Raises:
        AssertionError: If response time exceeds max_time
    """
    actual_time = response.elapsed.total_seconds()
    assert actual_time <= max_time, (
        f"Response time {actual_time:.3f}s exceeded maximum {max_time}s"
    )