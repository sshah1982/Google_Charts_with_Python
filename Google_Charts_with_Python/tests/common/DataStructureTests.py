# Sample data
data = [
    ['Task', 'Hours per Day'],
    ['Work', 11],
    ['Eat', 2],
    ['Commute', 2],
    ['Watch TV', 2],
    ['Sleep', 7]
]

# Test: Check data structure
def test_data_structure(data):
    assert isinstance(data, list), "Data should be a list"
    assert all(isinstance(row, list) for row in data), "Each row should be a list"
    assert len(data) > 0, "Data should not be empty"
    assert len(data[0]) > 0, "Data should have columns"
    return True

if test_data_structure(data):
    print("Data structure test passed")
else:
    print("Data structure test failed")