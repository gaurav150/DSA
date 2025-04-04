def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    count = 0
    vowels = 'aeiouAEIOU'
    for ele in s:
        if ele.isalpha() and ele not in vowels:
            count += 1
    return count

# Example usage:
if __name__ == "__main__":
    input_string = "Hello, how are you?"
    print(f"The number of consonants in '{input_string}' is: {count_consonants(input_string)}")
    input_string = "This is a test string."
    print(f"The number of consonants in '{input_string}' is: {count_consonants(input_string)}")
    input_string = "Count the consonants in this sentence."
    print(f"The number of consonants in '{input_string}' is: {count_consonants(input_string)}")