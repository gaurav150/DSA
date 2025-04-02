def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    lst = []
    for i in range(1, n + 1):   
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lst.append(spaces + stars+ spaces)
    return lst
# Example usage:
if __name__ == "__main__":
    n = 5
    pyramid_pattern = generate_pyramid(n)
    print(pyramid_pattern)