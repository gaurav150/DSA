'''
Reverse a List (Non-Slicing Approach)

You are given a list of integers. 
Write a Python program that reverses the
 list without using slicing (lst[::-1]).
   The program should return the reversed list.
'''

def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst.insert(0, item)
    return reversed_lst

# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    print(reverse_list(lst))  # Output: [5, 4, 3, 2, 1]

    lst = [10, 20, 30, 40]
    print(reverse_list(lst))  # Output: [40, 30, 20, 10]