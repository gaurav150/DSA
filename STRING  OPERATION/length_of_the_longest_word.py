'''
You are given a string s. Your task is to find the length of 
the longest word in the string. A word is defined as a sequence of 
characters separated by spaces.
 Do not use any built-in functions for string manipulation.
'''

def length_of_longest_word(s):
    max_length = 0
    current_length = 0
    
    for i in range(len(s)):
        if s[i] != ' ':
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    
    if current_length > max_length:
        max_length = current_length
    return max_length

# Example usage:
if __name__ == "__main__":
    input_string = "Hello, how are you?"
    print(f"The length of the longest word in '{input_string}' is: {length_of_longest_word(input_string)}")
    
    input_string = "This is a test string."
    print(f"The length of the longest word in '{input_string}' is: {length_of_longest_word(input_string)}")
    
    input_string = "Find the length of the longest word in this sentence."
    print(f"The length of the longest word in '{input_string}' is: {length_of_longest_word(input_string)}")