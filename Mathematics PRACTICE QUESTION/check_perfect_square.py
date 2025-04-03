"""
    Function to check if a number is a perfect square.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
def is_perfect_square(num):
    # Your code here
    if num < 0:
        return False
    if num == 0 or num == 1:
        return True
    i = 1
    
    while i * i <= num:
        square = i * i
        if  square == num:
            return True
        i += 1
        
    return False
# Test cases    

if __name__ == "__main__":
    # Test case 1: Check if 16 is a perfect square
    num = 16
    print(f"Is {num} a perfect square? {is_perfect_square(num)}")  # Expected output: True

    # Test case 2: Check if 20 is a perfect square
    num = 20
    print(f"Is {num} a perfect square? {is_perfect_square(num)}")  # Expected output: False

    # Test case 3: Check if -4 is a perfect square
    num = -4
    print(f"Is {num} a perfect square? {is_perfect_square(num)}")  # Expected output: False

    # Test case 4: Check if 0 is a perfect square
    num = 0
    print(f"Is {num} a perfect square? {is_perfect_square(num)}")  # Expected output: True

    # Test case 5: Check if 1 is a perfect square
    num = 1
    print(f"Is {num} a perfect square? {is_perfect_square(num)}")  # Expected output: True

    # Test case 6: Check if 25 is a perfect square
    num = 25
    print(f"Is {num} a perfect square? {is_perfect_square(num)}")  # Expected output: True