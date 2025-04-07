def count_down(n):
    """
    Function to return a list of integers from n to 1 using recursion.
    
    Parameters:
    n (int): The positive integer representing the starting point of the range.
    
    Returns:
    list: A list of integers from n to 1.
    """
    # Your code here
    if n == 0:
        return []
    else:
        ans = [n] + count_down(n-1)
        return ans
    
# Test cases
def test_count_down():
    assert count_down(0) == [], "Test case 0 failed"
    assert count_down(1) == [1], "Test case 1 failed"
    assert count_down(2) == [2, 1], "Test case 2 failed"
    assert count_down(3) == [3, 2, 1], "Test case 3 failed"
    assert count_down(4) == [4, 3, 2, 1], "Test case 4 failed"
    assert count_down(5) == [5, 4, 3, 2, 1], "Test case 5 failed"
    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_count_down()
    # Example usage
    n = 5
    print(f"The countdown from {n} is {count_down(n)}")