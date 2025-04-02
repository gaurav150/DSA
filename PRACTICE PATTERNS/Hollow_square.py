def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    lst = []
    for i in range(n):
        if i == 0 or i == n - 1:
            lst.append('*' * n)
        else:
            lst.append('*' + ' ' * (n - 2) + '*')
    return lst

# Example usage:
if __name__ == "__main__":
    for i in range(3, 11,2):
        print(f"n = {i}")
        hollow_square_pattern = generate_hollow_square(i)
        print(hollow_square_pattern)
    