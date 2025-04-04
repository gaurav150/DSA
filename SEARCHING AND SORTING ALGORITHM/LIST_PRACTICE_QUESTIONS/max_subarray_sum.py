def max_subarray_sum(arr):
    """
    Given an array of integers, find the maximum sum of any subarray.

    Parameters:
    arr (List[int]): List of integers.

    Returns:
    int: Maximum sum of any subarray.
    """
    # Implement the function
    if not arr:
        return 0
    max_sum = current_sum = arr[0]
    for i in range(1,len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test cases to validate the solution
def test_max_subarray_sum():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6, "Test case 1 failed"
    assert max_subarray_sum([1]) == 1, "Test case 2 failed"
    assert max_subarray_sum([5,4,-1,7,8]) == 23, "Test case 3 failed"
    assert max_subarray_sum([-1,-2,-3]) == -1, "Test case 4 failed"
    assert max_subarray_sum([]) == 0, "Test case 5 failed"
    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_max_subarray_sum()
    # Example usage
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(f"Max subarray sum in {arr} is: {max_subarray_sum(arr)}")
    
