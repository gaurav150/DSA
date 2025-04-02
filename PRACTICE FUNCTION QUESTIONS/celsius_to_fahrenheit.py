def celsius_to_fahrenheit(C):
    """
    Function to convert temperature from Celsius to Fahrenheit.
    
    Parameters:
    C (float): The temperature in Celsius.
    
    Returns:
    float: The temperature in Fahrenheit.
    """
    # Your code here
    temperature = (9/5) * C + 32
    return temperature


# Example usage
if __name__ == "__main__":
    # Test the function with an example
    celsius_temp = 25.0  # Example temperature in Celsius
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")