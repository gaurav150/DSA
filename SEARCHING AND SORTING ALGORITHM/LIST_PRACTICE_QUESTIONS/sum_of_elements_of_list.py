def sum_of_elements(lst):
    """
    Function to find the sum of all elements in the list.
    :param lst: List[int] -> List of integers
    :return: int -> The sum of all elements in the list
    """
    # TODO: Implement this function
    sum = 0
    for ele in lst:
        sum += ele
    return sum

# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(sum_of_elements(lst))  # Output: 15
    lst = [-1, -2, -3, -4, -5]
    print(sum_of_elements(lst))  # Output: -15
    lst = []
    print(sum_of_elements(lst))  # Output: 0