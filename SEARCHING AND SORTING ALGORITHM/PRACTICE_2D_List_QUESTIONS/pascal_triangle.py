def generate(numRows):
    """
    Function to generate the first numRows of Pascal's triangle.
    :param numRows: int -> Number of rows of Pascal's triangle to generate
    :return: List[List[int]] -> The first numRows of Pascal's triangle
    """
    # TODO: Implement this function
    triangle = []

    for row in range(numRows):
        # Start each row with a list containing '1'
        current_row = [1] * (row + 1)
        
        # Each element (except the first and last) is the sum of the two elements above it
        for j in range(1, row):
            current_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
        
        triangle.append(current_row)

    return triangle
# Test cases to validate the solution
def test_generate():
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], "Test case 1 failed"
    assert generate(0) == [], "Test case 2 failed"
    assert generate(1) == [[1]], "Test case 3 failed"
    assert generate(2) == [[1], [1, 1]], "Test case 4 failed"
    assert generate(3) == [[1], [1, 1], [1, 2, 1]], "Test case 5 failed"
    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_generate()
    # Example usage
    numRows = 5
    print(f"Pascal's triangle with {numRows} rows is: {generate(numRows)}")