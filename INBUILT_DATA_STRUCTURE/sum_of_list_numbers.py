'''
Sum of List Elements
Problem Description

Sum of List Elements

Write a Python function that calculates the sum of all elements in a given list of integers.

Parameters:

numbers (List of integers): The input list containing integers.

Returns:

An integer representing the sum of all elements in the input list.
'''
def sum_of_list_elements(numbers):
    return sum(numbers)

# Test cases
if __name__ == "__main__":
    # Example test case
    test_case = [1, 2, 3, 4, 5]
    print(f"Test case: {test_case}")
    print(f"Sum of elements: {sum_of_list_elements(test_case)}")  # Output: 15

    # Additional test cases
    test_case_2 = [-1, -2, -3, -4, -5]
    print(f"Test case: {test_case_2}")
    print(f"Sum of elements: {sum_of_list_elements(test_case_2)}")  # Output: -15

    test_case_3 = [0, 0, 0, 0]
    print(f"Test case: {test_case_3}")
    print(f"Sum of elements: {sum_of_list_elements(test_case_3)}")  # Output: 0

    test_case_4 = [10, -10, 20, -20]
    print(f"Test case: {test_case_4}")
    print(f"Sum of elements: {sum_of_list_elements(test_case_4)}")  # Output: 0