def printIndicesofanList(li,x,index = 0):
    if index == len(li):
        return
    if li[index] == x:
        print(index)
    printIndicesofanList(li, x, index + 1)

def print_all_indices(li,x):
    printIndicesofanList(li, x,0)


# Example usage
if __name__ == "__main__":
    # Test cases
    print_all_indices([1, 2, 3, 4, 5], 3)  # Output: 2
    print_all_indices([10, -2, 3, 10], 10)      # Output: 0 3
    print_all_indices([], 5)                # Output: -1 (empty list)
    print_all_indices([1, 2, 3, 4, 5], 5)  # Output: 4
    print_all_indices([1, 2, 3, 4, 5], 6)  # Output: -1 (not found)
    print_all_indices([1, 2, 3, 4, 5], 1)  # Output: 0
    print("all test cases passed!")

