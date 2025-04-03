def is_even(n):
    """
    Function to check if a number is even.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is even, False otherwise.
    """
    # Your code here
    if n % 2 == 0:
        return True
    return False

# Test cases
if __name__ == "__main__":
    # Test case 1: Check if 4 is even
    n = 4
    print(f"Is {n} even? {is_even(n)}")  # Expected output: True

    # Test case 2: Check if 7 is even
    n = 7
    print(f"Is {n} even? {is_even(n)}")  # Expected output: False

    # Test case 3: Check if -2 is even
    n = -2
    print(f"Is {n} even? {is_even(n)}")  # Expected output: True

    # Test case 4: Check if -3 is even
    n = -3
    print(f"Is {n} even? {is_even(n)}")  # Expected output: False