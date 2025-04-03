def count_vowel(s):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    # Your code here
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage:
if __name__ == "__main__":
    input_string = "Hello World"
    print(f"The number of vowels in '{input_string}' is: {count_vowel(input_string)}")