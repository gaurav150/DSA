def rotate_90(mat):
    """
    Function to rotate the matrix 90 degrees clockwise.
    :param mat: List[List[int]] -> 2D list representing the matrix
    :return: None -> Modifies the matrix in-place
    """
    n = len(mat)
    
    return [[mat[n-j-1][i] for j in range(n)] for i in range(n)]

    '''
    unction to check if mat can be rotated to match target.
    :param mat: List[List[int]] -> The original matrix
    :param target: List[List[int]] -> The target matrix
    :return: bool -> True if mat can be rotated to match target, otherwise False
    '''

def can_be_rotated(mat, target):
    # Check if the dimensions match
    if len(mat) != len(target) or len(mat[0]) != len(target[0]):
        return False
    
    # Check all four possible rotations
    for _ in range(4):
        if mat == target:
            return True
        mat = rotate_90(mat)
    
    return False
    
# Test cases to validate the solution
def test_can_be_rotated():
    # Test case 1: Original and target matrices are the same
    mat1 = [[1, 2], [3, 4]]
    target1 = [[1, 2], [3, 4]]
    assert can_be_rotated(mat1, target1) == True, "Test case 1 failed"

    # Test case 2: Original and target matrices are different but can be rotated
    mat2 = [[1, 2], [3, 4]]
    target2 = [[3, 1], [4, 2]]
    assert can_be_rotated(mat2, target2) == True, "Test case 2 failed"

    # Test case 3: Original and target matrices are different and cannot be rotated to match
    mat3 = [[1, 2], [3, 4]]
    target3 = [[5, 6], [7, 8]]
    assert can_be_rotated(mat3, target3) == False, "Test case 3 failed"

    # Test case 4: Original matrix is empty
    mat4 = []
    target4 = []
    assert can_be_rotated(mat4, target4) == True, "Test case 4 failed"

    # Test case 5: Original matrix is a single element
    mat5 = [[1]]
    target5 = [[1]]
    assert can_be_rotated(mat5, target5) == True, "Test case 5 failed"

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_can_be_rotated()
    # Example usage
    mat = [[1, 2], [3, 4]]
    target = [[3, 1], [4, 2]]
    print(f"Can {mat} be rotated to match {target}? {can_be_rotated(mat, target)}")