def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    # Your code here
    decimal_value = 0
    binary_str = binary_str[::-1]  # Reverse the string for easier processing
    for i in range(len(binary_str)):
        decimal_value += int(binary_str[i]) * (2 ** i)
    return decimal_value

# Test cases
if __name__ == "__main__":
    # Test case 1: Convert binary '1010' to decimal
    binary_str = '1010'
    print(f"Binary '{binary_str}' to decimal: {binary_to_decimal(binary_str)}")  # Expected output: 10

    # Test case 2: Convert binary '1111' to decimal
    binary_str = '1111'
    print(f"Binary '{binary_str}' to decimal: {binary_to_decimal(binary_str)}")  # Expected output: 15

    # Test case 3: Convert binary '0' to decimal
    binary_str = '0'
    print(f"Binary '{binary_str}' to decimal: {binary_to_decimal(binary_str)}")  # Expected output: 0

    # Test case 4: Convert binary '1' to decimal
    binary_str = '1'
    print(f"Binary '{binary_str}' to decimal: {binary_to_decimal(binary_str)}")  # Expected output: 1

    # Test case 5: Convert binary '1100100' to decimal
    binary_str = '1100100'
    print(f"Binary '{binary_str}' to decimal: {binary_to_decimal(binary_str)}")  # Expected output: 100