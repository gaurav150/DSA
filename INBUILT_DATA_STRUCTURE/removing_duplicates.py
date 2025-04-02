""""Remove Duplicates from a List

You are given a list of integers. Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements. The order of elements in the list should be maintained.

Parameters:

lst (List of integers): The list of integers from which duplicates should be removed.

Returns:

A list of integers where all duplicates have been removed, preserving the original order.

"""





def remove_duplicates(lst):
    # Your code goes here
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list
