def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    
    # Your code here
    if len(t) > len(s):
        return False
    for i in range(len(s) - len(t) + 1):
        for j in range(len(t)):
            if s[i + j] != t[j]:
                break
        else:
            return True
    return False

# Example usage:

if __name__ == "__main__":
    str1 = "Hello, how are you?"
    str2 = "how"
    print(f"Is '{str2}' a substring of '{str1}'? {is_substring(str1, str2)}")
    
    str1 = "This is a test string."
    str2 = "test"
    print(f"Is '{str2}' a substring of '{str1}'? {is_substring(str1, str2)}")
    
    str1 = "Count the words in this sentence."
    str2 = "words in"
    print(f"Is '{str2}' a substring of '{str1}'? {is_substring(str1, str2)}")
