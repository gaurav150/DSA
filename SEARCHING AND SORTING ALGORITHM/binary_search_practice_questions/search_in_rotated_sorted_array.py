'''
Description:
Given a sorted array that has been rotated, 
find the index of a given target value. 
The array was originally sorted in ascending order and 
then rotated at some pivot.

Parameters:

nums (List[int]): A list of integers sorted in ascending order 
but rotated at an unknown pivot.

target (int): The integer value to search for in the array.

Return Values:

int: The index of the target value in the array, or -1 
if the target is not in the array.

'''
def search(nums, target):
    left,right =0,len(nums) - 1
    while left <= right:
        mid = (left + right) //2
        if nums[mid] == target:
            return mid
            
        if nums[left] <= nums[mid]:
            # Left side is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                # Right side is sorted
                left  = mid + 1
            else:
                right = mid - 1
            
    return -1


# Example usage
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = search(nums, target)
    print("The index of the target value is:", result)  # Output: 4

    # Example usage with a different target
    target = 3
    result = search(nums, target)
    print("The index of the target value is:", result)  # Output: -1

    # Example usage with a different rotated array
    nums = [1,3]
    target = 3
    result = search(nums, target)
    print("The index of the target value is:", result)  # Output: 1
    