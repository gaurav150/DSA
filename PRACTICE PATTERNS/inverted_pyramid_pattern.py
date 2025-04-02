def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    lst = []
    for i in range(n, 0, -1):   
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lst.append(spaces + stars+ spaces)
    return lst
# Example usage:
if __name__ == "__main__":
    n = 5
    inverted_pyramid_pattern = generate_inverted_pyramid(n)
    print(inverted_pyramid_pattern)