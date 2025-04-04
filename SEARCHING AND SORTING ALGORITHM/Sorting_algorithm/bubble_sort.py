def bubbleSort(arr):
    n = len(arr)
    for passes in range(n):  # number of passes
                            # Last passes elements are already sorted
        for j in range(0, n-1-passes): # number of comparisons
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubbleSort(arr)
    print("Sorted array is:", sorted_arr)

'''
COMPLEXITY
Average Complexity	O(n2)
Best Case	O(n)
Worst Case	O(n2)
Space Complexity	O(1)
'''