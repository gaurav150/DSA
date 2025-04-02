def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(n):
        lst.append("*"*(i+1))
    return lst

# Example usage:
if __name__ == "__main__":
    n = 5
    triangle_pattern = generate_triangle(n)
    print(triangle_pattern)