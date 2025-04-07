def factorial(n):
    """
    Function to calculate the factorial of a non-negative integer n using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the factorial is to be calculated.
    
    Returns:
    int: The factorial of n.
    """
    # Your code here
    if n > -1:
        if n == 0 :
            return 1
        else:
            return n * factorial(n-1)
        

# Test cases
def test_factorial():
    assert factorial(0) == 1, "Test case 0 failed"
    assert factorial(1) == 1, "Test case 1 failed"
    assert factorial(2) == 2, "Test case 2 failed"
    assert factorial(3) == 6, "Test case 3 failed"
    assert factorial(4) == 24, "Test case 4 failed"
    assert factorial(5) == 120, "Test case 5 failed"
    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_factorial()
    # Example usage
    n = 5
    print(f"The factorial of {n} is {factorial(n)}")    

# The factorial of 5 is 120
# The factorial of 4 is 24
# The factorial of 3 is 6
# The factorial of 2 is 2
# The factorial of 1 is 1
# The factorial of 0 is 1
# All test cases passed!