def is_sorted(arr):
    """
    Function to check if the given array is sorted in non-decreasing order.
    :param arr: List[int] -> A list of integers
    :return: bool -> True if the array is sorted, False otherwise
    """
    # TODO: Implement this function
    n = len(arr)
    if n <= 1:
        return True
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(is_sorted(arr))  # Output: True

    arr = [5, 3, 2, 1]
    print(is_sorted(arr))  # Output: False

    arr = [1, 2, 2, 3, 4]
    print(is_sorted(arr))  # Output: True

    arr = []
    print(is_sorted(arr))  # Output: True