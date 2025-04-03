def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    
    return normalized_str == normalized_str[::-1]

# Example usage:
if __name__ == "__main__":
    input_string = "madam"
    print(f"Is '{input_string}' a palindrome? {is_palindrome(input_string)}")
    input_string = "hello"
    print(f"Is '{input_string}' a palindrome? {is_palindrome(input_string)}")
    input_string = "racecar"
    print(f"Is '{input_string}' a palindrome? {is_palindrome(input_string)}")