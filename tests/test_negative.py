from tests.helpers.api_helpers import make_request, validate_status_code
from tests.helpers.constants import ENDPOINTS

# NOTE: JSONPlaceholder is a lenient mock API and doesn't enforce strict validation.
# In a real API, these scenarios would return 400/422 error codes.

def test_invalid_endpoint_returns_404():
    """Test requesting non-existent endpoint returns 404"""
    response = make_request("GET", "/nonexistent")
    assert response.status_code == 404

def test_invalid_post_id_returns_404():
    """Test requesting non-existent posts returns 404"""
    response = make_request("GET", f"{ENDPOINTS['POSTS']}/99999")
    assert response.status_code == 404

def test_create_post_with_missing_fields():
    """Test creating post with missing required fields"""
    incomplete_data = {
        "userId": 1,
        "body": "Just a body, no title"
        # Missing "title"
    }
    
    response = make_request("POST", ENDPOINTS["POSTS"], json=incomplete_data)
    assert response.status_code == 201  # JSONPlaceholder is lenient

def test_create_post_with_invalid_data_types():
    """Test creating post with invalid data types"""
    invalid_data = {
        "userId": "not a number",  # Should be int
        "title": "Test",
        "body": "Test body"
    }
    
    response = make_request("POST", ENDPOINTS["POSTS"], json=invalid_data)
    assert response.status_code == 201 # JSONPlaceholder is lenient

def test_invalid_http_method():
    """Test using invalid HTTP method on endpoint"""
    response = make_request("BANANA", ENDPOINTS["POSTS"])
    assert response.status_code == 503