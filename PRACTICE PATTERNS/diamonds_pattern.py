def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    lst = []
    # Upper part of the diamond
    for i in range(1, n + 1):   
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lst.append(spaces + stars + spaces)
    # Lower part of the diamond
    for i in range(n - 1, 0, -1):   
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        lst.append(spaces + stars + spaces)
    return lst
# Example usage:
if __name__ == "__main__":
    n = 5
    diamond_pattern = generate_diamond(n)
    print(diamond_pattern)
# Output:
# ['     *     ', '    ***    ', '   *****   ', '  *******  ', ' ********* ', '***********', ' ********* ', '  *******  ', '   *****   ', '    ***    ', '     *     ']
