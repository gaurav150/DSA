'''
Check if a List 
is a Subset of Another List (Brute Force Approach)

You are given two lists of integers.
 Write a Python program that checks whether 
 the first list is a subset of the second list
   using a brute-force approach, without using the in keyword. 
   A list is considered a subset if all elements of the first 
   list are present in the second list.

Parameters:

lst1 (List of integers): The first list, which is being checked as a subset.

lst2 (List of integers): The second list, which is the list to compare against.

Returns:

A boolean value True if lst1 is a subset of lst2, otherwise False.
'''


def is_subset(lst1, lst2):
    
    for ele in lst1:
        found = False
        for item in lst2:
            if item == ele:
                found = True
                break
        if not found:
            
            return False
    return True

# Example usage:
lst1 = [1, 2, 3]    
lst2 = [3, 2, 1, 4, 5]
print(is_subset(lst1, lst2))  # Output: True
lst1 = [1, 2, 6]
lst2 = [3, 2, 1, 4, 5]
print(is_subset(lst1, lst2))  # Output: False
lst1 = [1, 2, 3]
lst2 = [3, 2, 1, 4, 5]  
print(is_subset(lst1, lst2))  # Output: True
lst1 = [1, 2, 3]
lst2 = [3, 2, 1, 4, 5]
print(is_subset(lst1, lst2))  # Output: True