def palindrome_helper(string, left, right):
    # Base case: if the left index is greater than or equal to the right index, it's a palindrome
    if left >= right:
        return True
    # Check if the characters at the left and right indices are equal
    if string[left] != string[right]:
        return False
    # Recursive case: move towards the center of the string
    return palindrome_helper(string, left + 1, right - 1)


def checkPalindrome(string):
    # Remove spaces and convert to lowercase for uniformity
    string = string.replace(" ", "").lower()
    # Call the helper function with the initial indices
    return palindrome_helper(string, 0, len(string) - 1)

# Example usage
string = "racecar"
result = checkPalindrome(string)
print(f"Is '{string}' a palindrome? {result}")