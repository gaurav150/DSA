def find_indices(arr, element):
    """
    Function to find all indices of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    list of int: A list containing all indices of the element in the array.
    """
    
    def helper(index):
        # Base case: if index is out of bounds, return an empty list
        if index >= len(arr):
            return []
        
        # Recursive case: check the current index and proceed to the next
        if arr[index] == element:
            return [index] + helper(index + 1)  # Include current index and continue
        else:
            return helper(index + 1)  # Skip current index and continue
    
    return helper(0)  # Start the recursion from index 0

# Example usage:
arr = [1, 2, 3, 2, 4, 2]
element = 2
print(find_indices(arr, element))  # Output: [1, 3, 5]
# Test cases
assert find_indices([1, 2, 3, 4, 5], 3) == [2], "Test case 1 failed"
assert find_indices([10, -2, 3, 10], 10) == [0, 3], "Test case 2 failed"
assert find_indices([], 5) == [], "Test case 3 failed"  # Empty list
assert find_indices([1, 2, 3, 4, 5], 5) == [4], "Test case 4 failed"  # Last element
assert find_indices([1, 2, 3, 4, 5], 6) == [], "Test case 5 failed"  # Not found
assert find_indices([1, 2, 3, 4, 5], 1) == [0], "Test case 6 failed"  # First element
assert find_indices([1, 2, 3, 2, 4, 2], 2) == [1, 3, 5], "Test case 7 failed"  # Multiple occurrences
assert find_indices([1, 2, 3, 4, 5], 0) == [], "Test case 8 failed"  # Not found
assert find_indices([1, 2, 3, 4, 5], 4) == [3], "Test case 9 failed"  # Middle element
assert find_indices([1, 2, 3, 4, 5], 2) == [1], "Test case 10 failed"  # Middle element
print("All test cases passed!")