def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    is_negative = n < 0  # Check if the number is negative
    n = abs(n)  # Work with the absolute value of n
    
    if n == 0:
        return "0"  # Return "0" for zero
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary  # Prepend the binary digit
        n //= 2  # Divide n by 2
    
    if is_negative:
        binary = "-" + binary  # Add negative sign if necessary
    
    return binary

# Example usage:
if __name__ == "__main__":
    print(int_to_binary(10))   # Output: "1010"
    print(int_to_binary(-10))  # Output: "-1010"
    print(int_to_binary(0))    # Output: "0"
    print(int_to_binary(255))  # Output: "11111111"
    print(int_to_binary(-255)) # Output: "-11111111"