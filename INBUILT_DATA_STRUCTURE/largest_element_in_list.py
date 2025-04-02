'''
Largest Element in a List
Find the Largest Element in a List

Write a Python function that finds and returns the largest element in a given list of integers.

Parameters:

numbers (List of integers): The input list containing integers.

Returns:

An integer representing the largest element in the input list.
'''

def largest_element_in_list(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest