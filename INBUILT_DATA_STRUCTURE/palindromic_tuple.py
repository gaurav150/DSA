'''
Palindromic Tuple
Check if Tuple is Palindromic

Design a Python function named
 is_palindromic_tuple to check 
 if a tuple is palindromic, 
 meaning it reads the same forwards and backwards.
'''



def is_palindromic_tuple(tup):
    start = 0
    end = len(tup) - 1
    while start <= end:
        if tup[start] != tup[end]:
            return False
        start += 1
        end -= 1    
        
    return True

# Example usage:
tup = (1, 2, 3, 2, 1)   
print(is_palindromic_tuple(tup))  # Output: True
tup = (1, 2, 3, 4, 5)
print(is_palindromic_tuple(tup))  # Output: False
tup = (1, 2, 3, 4, 5, 6)

print(is_palindromic_tuple(tup))  # Output: False

tup = (1, 2, 3, 4, 5, 6, 7)
print(is_palindromic_tuple(tup))  # Output: False