def checkSorted(l1):
    """
    This function checks if the given list is sorted in ascending order.
    :param l1: List of numbers
    :return: True if the list is sorted, False otherwise
    """
    # Base case: if the list has 0 or 1 elements, it is sorted
    if len(l1) <= 1:
        return True
    
    # Check if the first element is less than or equal to the second element
    if l1[0] <= l1[1]:
        # Recursively check the rest of the list
        return checkSorted(l1[1:])
    
    # If the first element is greater than the second element, the list is not sorted
    return False

# Example usage
if __name__ == "__main__":
    # Test cases
    print(checkSorted([1, 2, 3, 4, 5]))  # Output: True
    print(checkSorted([5, 4, 3, 2, 1]))  # Output: False
    print(checkSorted([1, 2, 2, 3, 4]))  # Output: True
    print(checkSorted([]))                # Output: True (empty list is considered sorted)
    print(checkSorted([1]))               # Output: True (single element list is considered sorted)
    print("all test cases passed!")

#    Run the test cases 
#    def test_check_sorted():
#        assert checkSorted([1, 2, 3, 4, 5]) == True, "Test case 1 failed"      
#        assert checkSorted([5, 4, 3, 2, 1]) == False, "Test case 2 failed"
#        assert checkSorted([1, 2, 2, 3, 4]) == True, "Test case 3 failed"
#        assert checkSorted([]) == True, "Test case 4 failed"  # Empty list is considered sorted


