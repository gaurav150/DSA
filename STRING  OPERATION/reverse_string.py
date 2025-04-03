def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    # Your code here
    reverse_string = ""
    for i in range(len(s)-1, -1, -1):
        reverse_string += s[i]
    return reverse_string
