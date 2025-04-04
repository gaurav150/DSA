def count_words(s):
    """
    Function to count the number of words in the input string.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    # Your code here
    count = 0
    word = False
    
    for ele in s:
        if ele != ' ':
            if not word:
                word = True
                count += 1
        else:
            word = False
    return count
    
# Example usage:
if __name__ == "__main__":
    input_string = "Hello, how are you?"
    print(f"The number of words in '{input_string}' is: {count_words(input_string)}")
    input_string = "This is a test string."
    print(f"The number of words in '{input_string}' is: {count_words(input_string)}")
    input_string = "Count the words in this sentence."
    print(f"The number of words in '{input_string}' is: {count_words(input_string)}")