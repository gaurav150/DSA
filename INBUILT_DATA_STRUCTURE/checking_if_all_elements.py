"""
Check if All Elements in a List are Unique

You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False.

Parameters:

lst (List of integers): The list of integers to check for uniqueness.

Returns:

A boolean value True if all elements in the list are unique, False otherwise.



"""


def check_unique(lst):
    a_set = set(lst)
    return len(lst) == len(a_set)


# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(check_unique(lst))  # Output: True

    lst = [1, 2, 3, 4, 5, 1]
    print(check_unique(lst))  # Output: False
