ansList = []
def updateAllIndicesofAnElementGlobalList(li,x,index = 0):
    if index == len(li):
        return 
    if li[index] == x:
        ansList.append(index)
    updateAllIndicesofAnElementGlobalList(li, x, index + 1)

# Example usage

if __name__ == "__main__":
    # Test cases
    updateAllIndicesofAnElementGlobalList([1, 2, 3, 4, 5], 3)  # Output: [2]
    print(ansList)
    ansList.clear()
    updateAllIndicesofAnElementGlobalList([10, -2, 3, 10], 10)      # Output: [0, 3]
    print(ansList)
    ansList.clear()
    updateAllIndicesofAnElementGlobalList([], 5)                # Output: [] (empty list)
    print(ansList)
    ansList.clear()
    updateAllIndicesofAnElementGlobalList([1, 2, 3, 4, 5], 5)  # Output: [4]
    print(ansList)
    ansList.clear()
    updateAllIndicesofAnElementGlobalList([1, 2, 3, 4, 5], 6)  # Output: [] (not found)
    print(ansList)
    ansList.clear()
    updateAllIndicesofAnElementGlobalList([1, 2, 3, 4, 5], 1)  # Output: [0]
    print(ansList)
    ansList.clear()
    updateAllIndicesofAnElementGlobalList([1, 2, 3, 4, 5], 2)  # Output: [1]
    print(ansList)
    ansList.clear()