def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    lst = []
    # Upper part of the sandglass
    for i in range(n, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lst.append(spaces + stars + spaces)
    # Lower part of the sandglass
    for i in range(2, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lst.append(spaces + stars + spaces)
    return lst
 