def binary_search(arr,target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (end + start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Example usage
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    target = 6
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")