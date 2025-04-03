'''
Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach)

You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. The difference is defined as the absolute value of the difference between two consecutive elements.

Parameters:

lst (List of integers): A list of integers.

Returns:

An integer representing the maximum difference between two consecutive elements.

'''

def max_consecutive_difference(lst):
    if len(lst) < 2:
        return 0
    max_diff = 0
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

# Example usage:
if __name__ == "__main__":
    lst = [1, 3, 7, 2, 5]
    print(max_consecutive_difference(lst))  # Output: 5 (|7 - 2|)

    lst = [10, 20, 30, 40]
    print(max_consecutive_difference(lst))  # Output: 10 (|30 - 40|)