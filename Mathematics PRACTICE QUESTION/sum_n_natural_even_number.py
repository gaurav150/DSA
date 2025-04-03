def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    total_sum = 0
    for i in range(1,n+1):
        total_sum += 2 * i
    return total_sum

# Test cases
if __name__ == "__main__":
    # Test case 1: Sum of first 5 even natural numbers
    n = 5
    print(f"Sum of first {n} even natural numbers: {sum_of_even_numbers(n)}")  # Expected output: 30

    # Test case 2: Sum of first 10 even natural numbers
    n = 10
    print(f"Sum of first {n} even natural numbers: {sum_of_even_numbers(n)}")  # Expected output: 110

    # Test case 3: Sum of first 0 even natural numbers
    n = 0
    print(f"Sum of first {n} even natural numbers: {sum_of_even_numbers(n)}")  # Expected output: 0