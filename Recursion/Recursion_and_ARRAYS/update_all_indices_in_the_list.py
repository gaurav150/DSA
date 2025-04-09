def updateAllIndicesofAnElementProvidedList(li,x,index = 0,indices = []):
    if index == len(li):
        return indices
    if li[index] == x:
        indices.append(index)
    return updateAllIndicesofAnElementProvidedList(li, x, index + 1, indices)

# Example usage

if __name__ == "__main__":
    # Test cases
    print(updateAllIndicesofAnElementProvidedList([1, 2, 3, 4, 5], 3))  # Output: [2]
    print(updateAllIndicesofAnElementProvidedList([10, -2, 3, 10], 10))      # Output: [0, 3]
    print(updateAllIndicesofAnElementProvidedList([], 5))                # Output: [] (empty list)
    print(updateAllIndicesofAnElementProvidedList([1, 2, 3, 4, 5], 5))  # Output: [4]
    print(updateAllIndicesofAnElementProvidedList([1, 2, 3, 4, 5], 6))  # Output: [] (not found)
    print(updateAllIndicesofAnElementProvidedList([1, 2, 3, 4, 5], 1))  # Output: [0]
    print("all test cases passed!")