def searchRange(nums, target):
    # Implement your solution here
    def findFirst(nums,target):
        left,right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return result
        
    def findLast(nums, target):
        """
        Find the last occurrence of the target using binary search.
        """
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
        
    start = findFirst(nums,target)
    end = findLast(nums,target)
    
    return [start,end]

# Example usage
if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    result = searchRange(nums, target)
    print("The starting and ending position of the target is:", result)  # Output: [3, 4]