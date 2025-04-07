def sum_of_natural_numbers(n):
    """
    Function to calculate the sum of the first n natural numbers using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the sum is to be calculated.
    
    Returns:
    int: The sum of the first n natural numbers.
    """
    # Base case: if n is 0, the sum is 0
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)
    
# Test cases
def test_sum_of_natural_numbers():
    assert sum_of_natural_numbers(0) == 0, "Test case 0 failed"
    assert sum_of_natural_numbers(1) == 1, "Test case 1 failed"
    assert sum_of_natural_numbers(2) == 3, "Test case 2 failed"
    assert sum_of_natural_numbers(3) == 6, "Test case 3 failed"
    assert sum_of_natural_numbers(4) == 10, "Test case 4 failed"
    assert sum_of_natural_numbers(5) == 15, "Test case 5 passed"
    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_sum_of_natural_numbers()
    # Example usage
    n = 5
    print(f"The sum of the first {n} natural numbers is {sum_of_natural_numbers(n)}")