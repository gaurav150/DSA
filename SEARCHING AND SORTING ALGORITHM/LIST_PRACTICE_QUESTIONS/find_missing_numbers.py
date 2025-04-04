def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    # Calculate the expected sum of numbers from 0 to n
    n = len(nums)
    expected_sum = n * (n + 1) // 2

    # Calculate the actual sum of the numbers in the list
    actual_sum = sum(nums)

    # The missing number is the difference between the expected and actual sums
    return expected_sum - actual_sum

    '''
    n = len(nums)
    number = 0
    lst = [ele for ele in range(n+1)]
    for ele in lst:
        if ele not in nums:
            number = ele 
    return number
    '''

# Example usage:
if __name__ == "__main__":
    nums = [3, 0, 1]
    print(find_missing_number(nums))  # Output: 2 (missing number is 2)
    nums = [0, 1]
    print(find_missing_number(nums))  # Output: 2 (missing number is 2)
    nums = [9,6,4,2,3,5,7,0,1]
    print(find_missing_number(nums))  # Output: 8 (missing number is 8)
