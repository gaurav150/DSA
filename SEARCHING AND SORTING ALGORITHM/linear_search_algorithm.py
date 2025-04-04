def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    target = 6
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")
    