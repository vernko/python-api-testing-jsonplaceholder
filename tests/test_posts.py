"""Tests for /posts endpoint"""

from tests.helpers.api_helpers import assert_response_time, make_request, validate_status_code
from tests.helpers.constants import ENDPOINTS, MAX_RESPONSE_TIME
from tests.helpers.schemas import POST_SCHEMA, validate_schema

def test_get_all_posts():
    """Test GET /posts returns list of posts"""
    response = make_request("GET", ENDPOINTS["POSTS"])
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
    assert_response_time(response, MAX_RESPONSE_TIME)

def test_get_post_by_id():
    """Test GET a single post by its ID returns the post with that ID"""
    response = make_request("GET", f"{ENDPOINTS['POSTS']}/1")
    
    assert response.status_code == 200

    post = response.json()
    validate_schema(post, POST_SCHEMA)
    assert_response_time(response, MAX_RESPONSE_TIME)

def test_create_a_post():
    """Test create a single post"""
    data = {
        "userId": 1,
        "title": "I Created This Post with Python",
        "body": "Creating this post for python to see if I can actually create a post has been super challenging."
    }
    response = make_request("POST", ENDPOINTS["POSTS"], json=data)
    validate_status_code(response, 201)

    created_post = response.json()
    validate_schema(created_post, POST_SCHEMA)
    assert_response_time(response, MAX_RESPONSE_TIME)

def test_update_a_post():
    """Test update a single post"""
    data = {
        "userId": 1,
        "title": "I Updated This Post with Python",
        "body": "Update this post using python to see if I can actually update a post. It's been super challenging."
    }
    response = make_request("PUT", f"{ENDPOINTS['POSTS']}/1", json=data)
    validate_status_code(response, 200)

    updated_post = response.json()
    validate_schema(updated_post, POST_SCHEMA)
    assert_response_time(response, MAX_RESPONSE_TIME)

def test_delete_a_post():
    """Test delete a single post"""
    response = make_request("DELETE", f"{ENDPOINTS['POSTS']}/1")
    validate_status_code(response, 200)
    assert response.json() == {}
    assert_response_time(response, MAX_RESPONSE_TIME)