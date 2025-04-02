def generate_inverted_triangle(n):
    """
    Function to return an inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(n, 0, -1):
        lst.append("*" * i)
    return lst

# Example usage:
if __name__ == "__main__":
    n = 5
    inverted_triangle_pattern = generate_inverted_triangle(n)
    print(inverted_triangle_pattern)