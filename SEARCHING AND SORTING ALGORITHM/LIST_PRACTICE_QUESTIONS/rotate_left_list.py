def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    if not ARR:
        return ARR
    D = D % len(ARR)  # Handle cases where D is greater than the length of the list
    return ARR[D:] + ARR[:D]

# Example usage:
if __name__ == "__main__":
    ARR = [1, 2, 3, 4, 5]
    D = 2
    print(rotate_left(ARR, D))  # Output: [3, 4, 5, 1, 2]
    ARR = [-1, -2, -3, -4, -5]
    D = 3
    print(rotate_left(ARR, D))  # Output: [-4, -5, -1, -2, -3]
    ARR = []
    D = 0
    print(rotate_left(ARR, D))  # Output: [] (an empty list remains empty)
