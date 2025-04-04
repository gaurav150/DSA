'''Description:
Given a list of integers, 
write a function to find the maximum element in the list.

Input Parameters:

lst (List[int]): A list of integers.

Output:

int: The maximum element in the list.'''

def find_maximum(lst):
    if not lst:
        return None
    max_element = lst[0]
    for ele in lst:
        if ele > max_element:
            max_element = ele
            
    return max_element

# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(find_maximum(lst))  # Output: 5
    lst = [-1, -2, -3, -4, -5]
    print(find_maximum(lst))  # Output: -1
    lst = []
    print(find_maximum(lst))  # Output: None