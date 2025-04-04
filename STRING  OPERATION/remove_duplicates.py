def remove_duplicates(s):
    """
    Function to remove duplicate characters from the input string.
    
    Parameters:
    s (str): The input string from which duplicates need to be removed.
    
    Returns:
    str: The modified string with duplicates removed.
    """
    # Your code here
    word = ''
    for ele in s:
        if ele not in word:
            word += ele
    return word

# Example usage:
if __name__ == "__main__":
    input_string = "Hello, how are you?"
    print(f"The string after removing duplicates from '{input_string}' is: {remove_duplicates(input_string)}")
    input_string = "This is a test string."
    print(f"The string after removing duplicates from '{input_string}' is: {remove_duplicates(input_string)}")
    input_string = "Remove the duplicates in this sentence."
    print(f"The string after removing duplicates from '{input_string}' is: {remove_duplicates(input_string)}")