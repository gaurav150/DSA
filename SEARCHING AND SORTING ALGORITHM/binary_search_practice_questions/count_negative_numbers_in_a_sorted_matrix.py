'''Description:
You are given an m x n matrix grid where each row 
and column is sorted in non-increasing order. 
Your task is to return the number of negative numbers present 
in the matrix.
Parameters:

grid (List[List[int]]): A 2D matrix with dimensions m x n, 
where each row and each column is sorted in non-increasing order.
Return Values:

Integer: The count of negative numbers in the matrix.
'''
def countNegatives(grid):
    '''count = 0
    for ele in grid:
        for elem in ele:
            if elem < 0:
                count += 1
    return count'''
    def count_negatives_in_row(row):
        left,right = 0,len(row)
        while left < right:
            mid= (left+right)//2
            if row[mid] < 0:
                right = mid
            else:
                left = mid + 1
        return len(row) - left
    
    count = 0
    for ele in grid:
        count += count_negatives_in_row(ele)
    return count

# Example usage
if __name__ == "__main__":
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[1,-1,-2,-3]]
    result = countNegatives(grid)
    print("Number of negative numbers in the matrix:", result)  # Output: 8