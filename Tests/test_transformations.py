import pytest
from transform import transform_data

@pytest.fixture
def sample_data():
    """Sample data matching API schema for testing."""
    return [
        {"userId": 1, "id": 1, "title": "Test title 1", "body": "Test body 1"},
        {"userId": 1, "id": 2, "title": "Test title 2", "body": "Test body 2"},
        {"userId": 2, "id": 3, "title": "Test", "body": "Test body 3"},
    ]

def test_transform_data(sample_data):
    """Test transformation logic with sample data."""
    transformed = transform_data(sample_data)
    
    # Should have one record per user
    assert len(transformed) == 2, "Expected 2 users in transformed data"
    
    # Check user 1 has 2 posts
    user1 = next(u for u in transformed if u['userId'] == 1)
    assert user1['postCount'] == 2, "User 1 should have 2 posts"
    
    # Check average title length calculation
    expected_avg = (len("Test title 1") + len("Test title 2")) / 2
    assert user1['avgTitleLength'] == expected_avg, "Incorrect average title length"