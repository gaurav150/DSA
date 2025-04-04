def rotate(matrix):
    """
    Function to rotate the matrix 90 degrees clockwise.
    :param matrix: List[List[int]] -> 2D list representing the matrix
    :return: None -> Modifies the matrix in-place
    """
    # TODO: Implement this function
    n = len(matrix)
    # First, transpose the matrix
     
    for i in range(n):
        for j in range(i , n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Then, reverse each row
    for i in range(n):
        matrix[i].reverse()
    
# Test cases to validate the solution
def test_rotate():
    # Test case 1
    matrix1 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    expected_output1 = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]
    rotate(matrix1)
    assert matrix1 == expected_output1, f"Test case 1 failed: expected {expected_output1}, got {matrix1}"

    # Test case 2: Single element matrix
    matrix2 = [[1]]
    expected_output2 = [[1]]
    rotate(matrix2)
    assert matrix2 == expected_output2, f"Test case 2 failed: expected {expected_output2}, got {matrix2}"

    # Test case 3: 2x2 matrix
    matrix3 = [
        [1, 2],
        [3, 4]
    ]
    expected_output3 = [
        [3, 1],
        [4, 2]
    ]
    rotate(matrix3)
    assert matrix3 == expected_output3, f"Test case 3 failed: expected {expected_output3}, got {matrix3}"

    # Test case 4: 3x3 matrix
    matrix4 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_output4 = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    rotate(matrix4)
    assert matrix4 == expected_output4, f"Test case 4 failed: expected {expected_output4}, got {matrix4}"

    # Test case 5: 4x4 matrix with negative numbers
    matrix5 = [
        [-1, -2, -3, -4],
        [-5, -6, -7, -8],
        [-9, -10, -11, -12],
        [-13, -14, -15, -16]
    ]
    expected_output5 = [
        [-13, -9, -5, -1],
        [-14, -10, -6, -2],
        [-15, -11, -7, -3],
        [-16, -12, -8, -4]
    ]
    rotate(matrix5)
    assert matrix5 == expected_output5, f"Test case 5 failed: expected {expected_output5}, got {matrix5}"

    print("All test cases passed!")

# Run the test
test_rotate()