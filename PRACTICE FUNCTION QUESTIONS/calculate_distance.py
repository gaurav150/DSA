def calculate_distance(speed, time):
    """
    Function to calculate the distance traveled by a vehicle.
    
    Parameters:
    speed (float): The speed of the vehicle.
    time (float): The time the vehicle has traveled.
    
    Returns:
    float: The distance traveled by the vehicle.
    """
    # Your code here
    return speed * time

# Example usage
if __name__ == "__main__":
    # Test the function with an example
    speed = 60.0  # Example speed in km/h
    time = 2.0    # Example time in hours
    distance = calculate_distance(speed, time)
    print(f"The distance traveled at a speed of {speed} km/h for {time} hours is {distance} km.")