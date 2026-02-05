"""Tests for /posts endpoint"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts():
    """Test GET /posts returns list of posts"""
    response = requests.get(f"{BASE_URL}/posts")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0