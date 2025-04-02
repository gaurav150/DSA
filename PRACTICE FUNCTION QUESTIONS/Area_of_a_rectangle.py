def area_of_rectangle(length, breadth):
    """
    Function to calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    breadth (float): The breadth of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    # Your code here
    return length * breadth

# Example usage
if __name__ == "__main__":
    # Test the function with an example
    length = 5.0  # Example length of the rectangle
    breadth = 3.0  # Example breadth of the rectangle
    area = area_of_rectangle(length, breadth)
    print(f"The area of the rectangle with length {length} and breadth {breadth} is {area}.")