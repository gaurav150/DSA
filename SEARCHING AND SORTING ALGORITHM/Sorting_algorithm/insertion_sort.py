'''
insertion sort algorithm
The insertion sort algorithm is a simple and 
intuitive sorting algorithm that builds a sorted array 
one element at a time. It works by dividing the input list 
into two parts: a sorted part and an unsorted part. 
The algorithm iteratively takes elements from the unsorted part 
and inserts them into the correct position in the sorted part.
'''

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr 

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    sorted_arr = insertion_sort(arr)
    print("Sorted array is:", sorted_arr)