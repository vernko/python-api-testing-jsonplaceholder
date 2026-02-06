"""Tests for /posts endpoint"""

import requests
from tests.helpers.api_helpers import make_request, validate_status_code
from tests.helpers.constants import ENDPOINTS

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts():
    """Test GET /posts returns list of posts"""
    response = make_request("GET", ENDPOINTS["POSTS"])
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0