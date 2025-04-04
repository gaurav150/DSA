def spiral_order(matrix):
    """
    Function to return the elements of the matrix in spiral order.
    :param matrix: List[List[int]] -> The input matrix
    :return: List[int] -> The elements in spiral order
    """
    # TODO: Implement this function
    result = []
    if not matrix:
        return result
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

## for testing the function
# Test cases to validate the solution
def display_result(matrix):
    result = spiral_order(matrix)
    print(result)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
display_result(matrix)  # Output should be [1, 2, 3, 6, 9, 8, 7, 4, 5]