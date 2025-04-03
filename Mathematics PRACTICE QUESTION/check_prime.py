def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Your code here
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    a = int(n **0.5) + 1
    for i in range(3,a,2):
        if n % a == 0:
            return False
    return True

# Test cases

if __name__ == "__main__":
    # Test case 1: Check if 5 is prime
    n = 5
    print(f"Is {n} prime? {is_prime(n)}")  # Expected output: True

    # Test case 2: Check if 4 is prime
    n = 4
    print(f"Is {n} prime? {is_prime(n)}")  # Expected output: False

    # Test case 3: Check if -3 is prime
    n = -3
    print(f"Is {n} prime? {is_prime(n)}")  # Expected output: False

    # Test case 4: Check if 13 is prime
    n = 13
    print(f"Is {n} prime? {is_prime(n)}")  # Expected output: True
    # Test case 5: Check if 1 is prime
    # n = 1
    # print(f"Is {n} prime? {is_prime(n)}")  # Expected output: False
    # Test case 6: Check if 0 is prime
    # n = 0  
