def selection_sort(lst):
    n = len(lst)
    for i in  range(n):
        min_index = i
        for j in range(i + 1,n):
            if (lst[j] < lst[min_index]):
                min_index = j
        
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

# Example usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorted_arr = selection_sort(arr)
    print("Sorted array is:", sorted_arr)