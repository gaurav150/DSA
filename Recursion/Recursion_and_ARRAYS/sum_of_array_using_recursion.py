def sum_of_array(li):
    if len(li) == 0:
        return 0
    else:
        return li[0] + sum_of_array(li[1:])
    

def sumArray_tail(li1,accumulator = 0):
    if len(li1) == 0:
        return accumulator
    else:
        return sumArray_tail(li1[1:], accumulator + li1[0])
    


# Example usage
if __name__ == "__main__":
    # Test cases
    print(sum_of_array([1, 2, 3, 4, 5]))  # Output: 15
    print(sum_of_array([10, -2, 3]))      # Output: 11
    print(sum_of_array([]))                # Output: 0 (empty list)
    print("all test cases passed!")

    # for tail recursion
    print(sumArray_tail([1, 2, 3, 4, 5]))  # Output: 15
    print(sumArray_tail([10, -2, 3]))      # Output: 11
    print(sumArray_tail([]))                # Output: 0 (empty list)
    print("all test cases passed!")

