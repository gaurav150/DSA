def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    lst = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        lst.append(spaces + numbers  + spaces)
    return lst
# Example usage:
if __name__ == "__main__":
    n = 5
    number_pyramid_pattern = generate_number_pyramid(n)
    print(number_pyramid_pattern)