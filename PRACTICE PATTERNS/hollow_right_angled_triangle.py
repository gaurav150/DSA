def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(n):
        if i == n-1:
            lst.append("*"*(i+1))
        elif i == 0:
            lst.append("*")
        else:
            lst.append("*" + " "*(i-1) + "*")
    return lst
# Example usage:
if __name__ == "__main__":
    n = 5
    hollow_right_angled_triangle_pattern = generate_hollow_right_angled_triangle(n)
    print(hollow_right_angled_triangle_pattern)
    