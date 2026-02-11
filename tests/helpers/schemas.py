POST_SCHEMA = {
    "fields": {
        "id": int,
        "title": str,
        "body": str,
        "userId": int
    },
    "required": ["id", "title", "body", "userId"]
}

def validate_schema(response_data, schema):
    """
    Validate response data against a schema.
    
    Args:
        response_data: Dictionary from API response (response.json())
        schema: Schema dictionary with 'fields' and 'required'
    
    Raises:
        AssertionError: If validation fails
    """
    # TODO: Check all required fields are present
    for field in schema["required"]:
        assert field in response_data, f"Required field '{field}' is missing"
    
    # TODO: Check each field has the correct type
    for field_name, expected_type in schema["fields"].items():
        actual_value = response_data[field_name]
        assert isinstance(actual_value, expected_type), \
            f"Field '{field_name}' should be {expected_type}, got {type(actual_value)}"