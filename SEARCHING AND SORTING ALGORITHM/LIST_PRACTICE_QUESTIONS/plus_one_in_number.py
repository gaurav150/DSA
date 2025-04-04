def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    # TODO: Implement this function
    n = len(digits)
    for i in range(n-1,-1,-1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# Example usage:
if __name__ == "__main__":
    digits = [1, 2, 3]
    print(plus_one(digits))  # Output: [1, 2, 4]
    digits = [9, 9, 9]
    print(plus_one(digits))  # Output: [1, 0, 0, 0]
    digits = [0]
    print(plus_one(digits))  # Output: [1] (incrementing zero gives one)
