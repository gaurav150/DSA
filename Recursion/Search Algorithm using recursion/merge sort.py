'''
merge sort using recursion
'''

def merge(arr, start, mid, end):
    i = start
    j = mid + 1
    ans = []
    
    while i <= mid and j <= end:
        if arr[i] < arr[j]:
            ans.append(arr[i])
            i += 1
        else:  
            ans.append(arr[j])
            j += 1
    
    while i <= mid:
        ans.append(arr[i])
        i += 1
    
    while j <= end:
        ans.append(arr[j])
        j += 1
    
    # Copy sorted items back to original array
    for k in range(len(ans)):
        arr[start + k] = ans[k]

def merge_sort_helper(arr, start, end):
    if start >= end:
        return
    
    mid = start + (end - start) // 2
    merge_sort_helper(arr, start, mid)
    merge_sort_helper(arr, mid + 1, end)
    merge(arr, start, mid, end)  # Add merge function call to combine sorted halves

def merge_sort(arr):
    """
    Function to perform merge sort on a list of integers using recursion.
    
    Parameters:
    arr (list of int): The list to be sorted.
    
    Returns:
    list of int: The sorted list.
    """
    merge_sort_helper(arr, 0, len(arr) - 1)
    return arr


l1 = [106,95,12,10,9,1]
sorted_array = merge_sort(l1)
print(sorted_array)