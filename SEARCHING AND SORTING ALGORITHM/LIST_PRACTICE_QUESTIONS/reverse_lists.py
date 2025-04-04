def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    '''
    reversed_lst = []
    if not lst:
        return []
    for ele in lst:
        reversed_lst.insert(0,ele)
    return reversed_lst '''
    
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left],lst[right] = lst[right],lst[left]
        left += 1
        right -= 1
    return lst

# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(reverse_list(lst))  # Output: [5, 4, 3, 2, 1]
    lst = [-1, -2, -3, -4, -5]
    print(reverse_list(lst))  # Output: [-5, -4, -3, -2, -1]
    lst = []
    print(reverse_list(lst))  # Output: [] (an empty list remains empty)