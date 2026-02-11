"""Tests for posts for schemas"""

import pytest
from tests.helpers.api_helpers import make_request, validate_status_code
from tests.helpers.constants import ENDPOINTS
from tests.helpers.schemas import POST_SCHEMA, validate_schema

def test_post_has_correct_type():
    """Test GET a single post and validatates it has the correct types"""
    response = make_request("GET", f"{ENDPOINTS['POSTS']}/1")

    post = response.json()
    validate_schema(post, POST_SCHEMA)

def test_required_fields_must_be_present():
    """Test that validation fails when required fields are missing"""
    incomplete_post = {
        "id": 1,
        "body": "test body",
        "userId": 1
        # Missing "title"!
    }

    with pytest.raises(AssertionError):
        validate_schema(incomplete_post, POST_SCHEMA)

def test_extra_fields_dont_break_validation():
    """Test that validation passes even with extra fields"""
    post_with_extra_fields = {
        "id": 1,
        "title": "test",
        "body": "test body",
        "userId": 1,
        "extraField": "this shouldn't break validation"  # Extra field
    }
    
    # Should not raise an error
    validate_schema(post_with_extra_fields, POST_SCHEMA)