def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    lst = []
    for i in range(n):
        lst.append('*'* n)
    return lst

# Example usage:
if __name__ == "__main__":
    n = 5
    square_pattern = generate_square(n)
    print(square_pattern)