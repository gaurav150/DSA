def calculate_y(slope, intercept, x):
    """
    Function to calculate the value of y using the slope-intercept form of a line.
    
    Parameters:
    slope (float): The slope of the line.
    intercept (float): The y-intercept of the line.
    x (float): The value of x for which y needs to be calculated.
    
    Returns:
    float: The calculated value of y.
    """
    
    y = slope * x + intercept
    
    return y

# Example usage
if __name__ == "__main__":
    # Test the function with an example
    slope = 2.0      # Example slope of the line
    intercept = 3.0  # Example y-intercept of the line
    x_value = 5.0    # Example value of x
    y_value = calculate_y(slope, intercept, x_value)
    print(f"The value of y for x = {x_value} is {y_value}.")