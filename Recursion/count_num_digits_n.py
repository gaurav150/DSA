def count_digits(n):
    """
    Function to find the number of digits in a number using recursion.
    
    Parameters:
    n (int): The positive integer whose digits are to be counted.
    
    Returns:
    int: The number of digits in the integer.
    """
    # Your code here
    if n == 0:
        return 1
    elif n < 10:
        return 1
    else:
        return 1 + count_digits(n//10)
    
# Test cases
def test_count_digits():
    assert count_digits(0) == 1, "Test case 0 failed"
    assert count_digits(1) == 1, "Test case 1 failed"
    assert count_digits(12) == 2, "Test case 2 failed"
    assert count_digits(123) == 3, "Test case 3 failed"
    assert count_digits(1234) == 4, "Test case 4 failed"
    assert count_digits(12345) == 5, "Test case 5 failed"
    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_count_digits()
    # Example usage
    n = 12345
    print(f"The number of digits in {n} is {count_digits(n)}")