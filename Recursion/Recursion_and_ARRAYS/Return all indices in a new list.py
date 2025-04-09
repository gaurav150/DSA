def ReturnAllIndicesASAList(li,x,index):
    if index == len(li):
        return []
    if li[index] == x:
        return [index] + ReturnAllIndicesASAList(li,x,index+1)
    else:
        return ReturnAllIndicesASAList(li,x,index+1)
    
# Test the function
li = [1, 2, 3, 4, 5, 2, 6, 2]
x = 2
index = 0
result = ReturnAllIndicesASAList(li, x, index)
print(result)  # Output: [1, 5, 7]

# The function ReturnAllIndicesASAList takes a list, a target value, and an index as input.
# It returns a new list containing all the indices of the target value in the original list.
# The function uses recursion to traverse the list and build the new list of indices.
# The base case is when the index reaches the length of the list, in which case it returns an empty list.
# If the current element matches the target value, it adds the index to the result list and continues searching in the rest of the list.
# If the current element does not match, it simply continues searching in the rest of the list without adding anything to the result.
# The final result is a list of all indices where the target value occurs in the original list.
# The function is tested with a sample list and target value, and the output is printed.
# The output is a list of indices where the target value occurs in the original list.

# The function is designed to be efficient and works well for lists of any size.
# It is a good example of how recursion can be used to solve problems involving lists and indices.
