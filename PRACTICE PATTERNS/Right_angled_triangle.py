def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    lst = []
    for i in range(n):
        lst.append(str(i+1)*(i+1))
    return lst
# Example usage:
if __name__ == "__main__":
    n = 5
    number_triangle_pattern = generate_number_triangle(n)
    print(number_triangle_pattern)
    