'''
Sorting using recursion

QUick SORT
Quick sort is a divide-and-conquer algorithm
that sorts an array by selecting a 'pivot' element
and partitioning the other elements into two sub-arrays according
to whether they are less than or greater than the pivot. 
The sub-arrays are then sorted recursively.
'''
def partitionFunction(li,start,end):
    pivot = li[end]
    i = start
    right_position = start
    while i <= end -1:
        if li[i] < pivot:
            right_position += 1
        i += 1
    li[right_position], li[end] = li[end], li[right_position]

    pivot_index = right_position

    # now make sure that all the elements to the left of pivot_index
    #  are smaller than pivot
    # and all the elements to the right of pivot_index are larger
    #  than pivot

    while start < pivot_index and end > pivot_index:
        if li[start] < li[pivot_index]:
            start += 1
        elif li[end] >= li[pivot_index]:
            end -= 1
        else:
            li[start], li[end] = li[end], li[start]
            start += 1
            end -= 1
    return pivot_index
        



def QuickSort(li,start,end):
    if  start >= end:
        return
    pivot_index = partitionFunction(li,start,end)
    QuickSort(li,start,pivot_index-1)
    QuickSort(li,pivot_index+1,end)
    return


li = [3,6,7,2,1,4,5,4]
QuickSort(li,0,len(li)-1)
print(li)