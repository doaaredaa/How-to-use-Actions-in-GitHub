import pytest
import requests
from extract import fetch_data

def test_api_response():
    """Test that API returns status code 200."""
    test_url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(test_url)
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"

def test_fetch_data_function():
    """Test our fetch_data function with a known good endpoint."""
    test_url = "https://jsonplaceholder.typicode.com/posts/1"
    data = fetch_data(test_url)
    assert isinstance(data, dict), "Expected dictionary response"
    assert 'userId' in data, "Response missing expected field 'userId'"