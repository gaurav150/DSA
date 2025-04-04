def matrix_reshape(mat, r, c):
    """
    Function to reshape a matrix.
    :param mat: List[List[int]] -> The original matrix
    :param r: int -> Number of rows in reshaped matrix
    :param c: int -> Number of columns in reshaped matrix
    :return: List[List[int]] -> The reshaped matrix or original matrix if not possible
    """
    # TODO: Implement this function
    original_rows = len(mat)
    original_cols = len(mat[0]) if mat else 0


    if original_rows * original_cols != r * c:
        return mat
    
    reshaped_matrix = []
    current_row = []
    for i in range(original_rows):
        for j in range(original_cols):
            current_row.append(mat[i][j])
            if len(current_row) == c:
                reshaped_matrix.append(current_row)
                current_row = []
    if current_row:
        reshaped_matrix.append(current_row)
    return reshaped_matrix


# Test cases to validate the solution

def test_matrix_reshape():
    # Test case 1: Reshape possible
    mat1 = [
        [1, 2],
        [3, 4]
    ]
    r1, c1 = 1, 4
    expected_output1 = [[1, 2, 3, 4]]
    assert matrix_reshape(mat1, r1, c1) == expected_output1, "Test case 1 failed"

    # Test case 2: Reshape not possible
    mat2 = [
        [1, 2],
        [3, 4]
    ]
    r2, c2 = 2, 3
    expected_output2 = [
        [1, 2],
        [3, 4]
    ]
    assert matrix_reshape(mat2, r2, c2) == expected_output2, "Test case 2 failed"

    # Test case 3: Empty matrix
    mat3 = []
    r3, c3 = 0, 0
    expected_output3 = []
    assert matrix_reshape(mat3, r3, c3) == expected_output3, "Test case 3 failed"

    # Test case 4: Single element matrix
    mat4 = [[5]]
    r4, c4 = 1, 1
    expected_output4 = [[5]]
    assert matrix_reshape(mat4, r4, c4) == expected_output4, "Test case 4 failed"

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_matrix_reshape()
    # Example usage
    mat = [
        [1, 2],
        [3, 4]
    ]
    r = 1
    c = 4
    reshaped = matrix_reshape(mat, r, c)
    print(reshaped)  # Output: [[1, 2, 3, 4]]
