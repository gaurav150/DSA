def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """
    # Your code here
    lst = []
    for i in range(n):
        lst.append('*' * m)
    return lst

# Example usage:
if __name__ == "__main__":
    n = 5
    m = 10
    rectangle_pattern = generate_rectangle(n, m)
    print(rectangle_pattern)