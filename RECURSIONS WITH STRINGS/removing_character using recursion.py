def remove_character(string,char):
    # Base case: if the string is empty, return an empty string
    if not string:
        return ""
    
    # Check if the first character is the one to be removed
    if string[0] == char:
        # If it is, skip it and call the function recursively on the rest of the string
        return remove_character(string[1:], char)
    else:
        # If it's not, keep it and call the function recursively on the rest of the string
        return string[0] + remove_character(string[1:], char)
    
# Example usage
input_string = "Hello World!"
char_to_remove = "l"
result = remove_character(input_string, char_to_remove)
print(f"Original string: {input_string}")
print(f"String after removing '{char_to_remove}': {result}")
# Output:
# Original string: Hello World!
# String after removing 'o': Hell Wrld!