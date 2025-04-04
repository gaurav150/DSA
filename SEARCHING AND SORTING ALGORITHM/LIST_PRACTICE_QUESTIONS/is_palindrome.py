def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    if not lst:
        return True
    left , right = 0 , len(lst)-1
    
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage:
if __name__ == "__main__":
    lst = [1, 2, 3, 2, 1]
    print(is_palindrome(lst))  # Output: True
    lst = [1, 2, 3, 4, 5]
    print(is_palindrome(lst))  # Output: False
    lst = []
    print(is_palindrome(lst))  # Output: True (an empty list is considered a palindrome)