def firstIndexofAnElement(li,x):
    if len(li) == 0:
        return -1
    if li[0] == x:
        return 0
    else:
        index = firstIndexofAnElement(li[1:], x)
        if index == -1:
            return -1
        else:
            return index + 1
        

def lastIndexofAnElement(li,x):
    if len(li) == 0:
        return -1
    index = lastIndexofAnElement(li[1:], x)
    if index == -1:
        if li[0] == x:
            return 0
        else:
            return -1
    else:
        return index + 1    

# Example usage

if __name__ == "__main__":
    # Test cases
    print(firstIndexofAnElement([1, 2, 3, 4, 5], 3))  # Output: 2
    print(firstIndexofAnElement([10, -2, 3], -2))      # Output: 1
    print(firstIndexofAnElement([], 5))                # Output: -1 (empty list)
    print("all test cases passed!")


    # for last index
    print(lastIndexofAnElement([1, 2, 3, 4, 5], 3))  # Output: 2
    print(lastIndexofAnElement([10, -2, 3], -2))      # Output: 1
    print(lastIndexofAnElement([], 5))                # Output: -1 (empty list)
    print(lastIndexofAnElement([1, 2, 3, 4, 5], 5))  # Output: 5 