from tests.helpers.api_helpers import make_request
from tests.helpers.constants import ENDPOINTS, ACCEPTABLE_RESPONSE_TIME

def test_average_response_time():
    """Test that average response time is acceptable over multiple requests"""
    num_requests = 10
    total_time = 0
    
    for i in range(num_requests):
        response = make_request("GET", f"{ENDPOINTS['POSTS']}/1")
        total_time += response.elapsed.total_seconds()
    
    average_time = total_time / num_requests
    
    # Assert average is under acceptable time
    assert average_time <= ACCEPTABLE_RESPONSE_TIME, \
        f"Average response time {average_time:.3f}s exceeded {ACCEPTABLE_RESPONSE_TIME}s"
    
def test_95_percent_requests_meet_threshold():
    num_requests = 20
    successful_requests = 0  # Counter for "fast enough" requests
    
    for i in range(num_requests):
        response = make_request("GET", f"{ENDPOINTS['POSTS']}/1")
        
        # Was this request fast enough?
        if response.elapsed.total_seconds() <= ACCEPTABLE_RESPONSE_TIME:
            successful_requests += 1  # Count it!
    
    # Calculate percentage
    success_rate = (successful_requests / num_requests) * 100
    # Example: 19 out of 20 = (19/20) * 100 = 95%
    
    # At least 95% should be fast
    assert success_rate >= 95