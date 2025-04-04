'''Description:
Given a sorted array that has been rotated, 
find the minimum element in the array. 
The array was originally sorted in ascending order 
and then rotated at some pivot.
The minimum element is the point where the rotation occurs.
This problem can be solved using binary search
Parameters:

nums (List[int]): A list of integers sorted in ascending order 
but rotated at an unknown pivot.
Return Values:
int: The minimum element in the rotated sorted array.'''

def findMin(nums):
    left,right = 0 , len(nums) - 1
    while left < right :
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return nums[left]
    
# Example usage
if __name__ == "__main__":
    nums = [3,4,5,1,2]
    result = findMin(nums)
    print("The minimum element in the rotated sorted array is:", result)  # Output: 1

# Example usage with a different rotated array

    nums = [4,5,6,7,0,1,2]
    result = findMin(nums)
    print("The minimum element in the rotated sorted array is:", result)  # Output: 0
