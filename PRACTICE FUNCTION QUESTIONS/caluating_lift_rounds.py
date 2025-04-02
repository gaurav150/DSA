def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    # Your code here
    if n <= 0 or capacity <= 0:
        return 0  # No rounds needed if there are no people or capacity is zero
    rounds = n // capacity  # Full rounds
    if n % capacity != 0:
        rounds += 1  # Add one more round for remaining people
    return rounds