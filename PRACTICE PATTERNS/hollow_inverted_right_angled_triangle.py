def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(n, 0, -1):
        if i == n:
            lst.append("*"*n)
        elif i == 1:
            lst.append("*")
        else:
            lst.append("*" + " "*(i-2) + "*")
    return lst
# Example usage:
if __name__ == "__main__":
    n = 5
    hollow_inverted_right_angled_triangle_pattern = generate_hollow_inverted_right_angled_triangle(n)
    print(hollow_inverted_right_angled_triangle_pattern)