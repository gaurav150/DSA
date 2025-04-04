'''
You are given two strings s and t. 
Your task is to determine if string t is a subsequence of string s. 
A subsequence of a string is a new string that is formed 
from the original string by deleting some (or no) characters 
without changing the order of the remaining characters.

'''

def is_subsequence(s, t):
    i, j = 0, 0  # Initialize two pointers for s and t
    
    # Loop through the original string s
    while i < len(s) and j < len(t):
        # If the characters match, move the pointer for t
        if s[i] == t[j]:
            j += 1
        # Always move the pointer for s
        i += 1
    
    # If we've matched all characters of t, return True
    return j == len(t)


# Example usage:


if __name__ == "__main__":
    str1 = "abcde"
    str2 = "ace"
    print(f"Is '{str2}' a subsequence of '{str1}'? {is_subsequence(str1, str2)}")
    
    str1 = "abcde"
    str2 = "aec"
    print(f"Is '{str2}' a subsequence of '{str1}'? {is_subsequence(str1, str2)}")
    
    str1 = "hello world"
    str2 = "hlo wrd"
    print(f"Is '{str2}' a subsequence of '{str1}'? {is_subsequence(str1, str2)}")
    str1 = "abcdefg"
    str2 = "aceg"
    print(f"Is '{str2}' a subsequence of '{str1}'? {is_subsequence(str1, str2)}")
