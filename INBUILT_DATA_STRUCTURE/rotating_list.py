'''
Rotate a List (Without Slicing)

You are given a list of integers and an integer k. 
Write a Python function to rotate the list to the right by k 
positions without using slicing. A rotation shifts elements 
from the end of the list to the front.

Parameters:

lst (List of integers): The list to be rotated.

k (Integer): The number of positions to rotate the list.

Returns:

A list of integers rotated by k positions.
'''

def rotate_list(lst, k):

    n = len(lst)
    rotate_list = [0] * n  # Initialize a new list of the same size
    if n == 0:
        return lst  # Return the original list if it's empty
    if k < 0:
        raise ValueError("k must be a non-negative integer")
    if k >= n:  
        k = k % n
          
    for i in range(n):
        new_index = (i + k) % n
        rotate_list[new_index] = lst[i]
    return rotate_list

# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    k = 2
    print(rotate_list(lst, k))  # Output: [4, 5, 1, 2, 3]

    lst = [10, 20, 30, 40]
    k = 3
    print(rotate_list(lst, k))  # Output: [30, 40, 10, 20]