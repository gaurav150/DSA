'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.

The first integer of each row is greater than the last integer of the previous row.

Write a function that takes an integer target and returns True if target is in matrix, or False otherwise. You must solve this problem with a time complexity better than O(m * n).

'''

def search_matrix(matrix, target):
    """
    Function to search for a target in the matrix.
    :param matrix: List[List[int]] -> The input matrix
    :param target: int -> The target value to search for
    :return: bool -> True if target is found, False otherwise
    """
    # TODO: Implement this function
    if not matrix or not matrix[0]:
        return False
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    left ,right = 0 , rows * cols - 1
    
    while left  <= right:
        mid = (left + right) // 2
        row = mid // cols
        col = mid % cols
        
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Test cases to validate the solution
def test_search_matrix():
    # Test case 1: Target found in the matrix
    matrix1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
        [60, 70, 80, 90]
    ]
    target1 = 3
    assert search_matrix(matrix1, target1) == True, "Test case 1 failed"

    # Test case 2: Target not found in the matrix
    matrix2 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
        [60, 70, 80, 90]
    ]
    target2 = 13
    assert search_matrix(matrix2, target2) == False, "Test case 2 failed"

    # Test case 3: Empty matrix
    matrix3 = []
    target3 = 5
    assert search_matrix(matrix3, target3) == False, "Test case 3 failed"

    # Test case 4: Single element matrix (target found)
    matrix4 = [[5]]
    target4 = 5
    assert search_matrix(matrix4, target4) == True, "Test case 4 failed"

    # Test case 5: Single element matrix (target not found)
    matrix5 = [[10]]
    target5 = 5
    assert search_matrix(matrix5, target5) == False, "Test case 5 failed"

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_search_matrix()
    # Example usage
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
        [60, 70, 80, 90]
    ]
    target = 3
    print(search_matrix(matrix, target))  # Output should be True