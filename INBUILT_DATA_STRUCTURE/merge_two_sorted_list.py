
'''You are given two sorted lists of integers. 
Write a Python function to merge these two 
sorted lists into one sorted list.
 The resulting list should also be in non-decreasing order.'''



def merge_two_sorted_lists(list1, list2):
    merged_list = []
    i,j = 0,0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements from list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    
    # Append remaining elements from list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list

# Example usage:
if __name__ == "__main__":
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8]
    print(merge_two_sorted_lists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

    list1 = [10, 20, 30]
    list2 = [5, 15, 25]
    print(merge_two_sorted_lists(list1, list2))  # Output: [5, 10, 15, 20, 25, 30]