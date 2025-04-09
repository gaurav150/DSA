def LinearSearchUsingRecursion(arr, target, index):
    # Base case: if index is equal to the length of the array, return -1
    if index == len(arr):
        return -1
    # If the current element matches the target, return the index
    if arr[index] == target:
        return index
    # Recursively call the function with the next index
    return LinearSearchUsingRecursion(arr, target, index + 1)

def linear_search(arr, target):
    """
    Function to perform linear search on an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    target (int): The element to search for.
    
    Returns:
    bool: True if target is found, False otherwise.
    """
    # Your code here
    def recursive_search(index):
        if index >= len(arr):
            return False
        if arr[index] == target:
            return True
        return recursive_search(index + 1)
        
    return recursive_search(0)



# Test the function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
index = 0
result = LinearSearchUsingRecursion(arr, target, index)
print(result)  # Output: 4 (the index of the target element in the array)

# The function LinearSearchUsingRecursion takes an array, a target value, and an index as input.

# test the linear_search function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = linear_search(arr, target)
print("linear search result without using index as parameter",result)  # Output: True (the target element is found in the array)