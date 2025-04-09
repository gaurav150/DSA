def BinarySearchUsingRecursion(li, x, start, end):
    if start > end:
        return False  # Element not found

    mid = start + (end - start) // 2

    if li[mid] == x:
        return True  # Element found
    elif li[mid] < x:
        return BinarySearchUsingRecursion(li, x, mid + 1, end)  # Search in the right half
    else:
        return BinarySearchUsingRecursion(li, x, start, mid - 1)  # Search in the left half

def BinarySearcUsingRecursion(li,x):
    return BinarySearchUsingRecursion(li, x, 0, len(li) -1 )

# Test the function
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5
result = BinarySearcUsingRecursion(li, x)
print(result)  # Output: True (the target element is found in the array)

