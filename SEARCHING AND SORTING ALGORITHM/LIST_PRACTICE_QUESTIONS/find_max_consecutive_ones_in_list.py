def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's
    """
    # TODO: Implement this function
    max_count = 0
    current_count = 0
    for ele in nums:
        if ele == 1:
            current_count += 1
        else:
            max_count = max(max_count,current_count)
            current_count = 0
    max_count = max(max_count,current_count)
    return max_count

# Test cases to validate the solution
def test_find_max_consecutive_ones():
    assert find_max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3, "Test case 1 failed"
    assert find_max_consecutive_ones([1, 0, 1, 1, 0, 1]) == 2, "Test case 2 failed"
    assert find_max_consecutive_ones([0, 0, 0]) == 0, "Test case 3 failed"
    assert find_max_consecutive_ones([1]) == 1, "Test case 4 failed"
    assert find_max_consecutive_ones([]) == 0, "Test case 5 failed"
    print("All test cases passed!")


# Run the test cases
if __name__ == "__main__":
    test_find_max_consecutive_ones()
    # Example usage
    nums = [1, 1, 0, 1, 1, 1]
    print(f"Max consecutive ones in {nums} is: {find_max_consecutive_ones(nums)}")