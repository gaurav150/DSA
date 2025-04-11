def calculate_special_sum(arr, index, prefix_sum):
    n = len(arr)
    special_sum = 0
    count = 1
    current_index = index

    while current_index + count <= n:
        # Use prefix sum for O(1) range sum
        group_sum = prefix_sum[current_index + count] - prefix_sum[current_index]
        special_sum += group_sum
        current_index += count
        count += 1

    return special_sum

def find_best_index_and_special_sum(arr):
    n = len(arr)
    # Precompute prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    max_special_sum = float('-inf')
    for i in range(n):
        special_sum = calculate_special_sum(arr, i, prefix_sum)
        max_special_sum = max(max_special_sum, special_sum)

    return max_special_sum

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output result
print(find_best_index_and_special_sum(arr))

'''
5
1 3 1 2 5
output 8

10
2 1 3 9 2 4 -10 -9 1 3
output 9

'''
'''
You are given an array 
 of 
 elements. Now you need to choose the best index of this array 
. An index of the array is called best if the special sum of this index is maximum across the special sum of all the other indices.

To calculate the special sum for any index 
 , you pick the first element that is 
 and add it to your sum. Now you pick next two elements i.e. 
 and 
 and add both of them to your sum. Now you will pick the next 
 elements and this continues till the index for which it is possible to pick the elements. For example:

If our array contains 
 elements and you choose index to be 
 then your special sum is denoted by -
 , beyond this its not possible to add further elements as the index value will cross the value 
.

Find the best index and in the output print its corresponding special sum. Note that there may be more than one best indices but you need to only print the maximum special sum.

Input
First line contains an integer 
 as input. Next line contains 
 space separated integers denoting the elements of the array 
.
Output
In the output you have to print an integer that denotes the maximum special sum
'''