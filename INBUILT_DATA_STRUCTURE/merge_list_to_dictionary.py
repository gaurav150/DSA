
'''Merge Lists to Dictionary

Design a Python function named 
merge_lists_to_dictionary to 
merge two lists into a dictionary
 where elements from the first list 
 act as keys and elements from the 
 second list act as values.
'''

def merge_lists_to_dictionary(keys, values):
    f_dict = {}
    i = len(keys)
    j = len(values)
    
    if i != j:
        return False
    for k in range(len(keys)):
        f_dict[keys[k]] = values[k]
            
    return f_dict

# Example usage:
if __name__ == "__main__":
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    print(merge_lists_to_dictionary(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3}

    keys = ['x', 'y', 'z']
    values = [10, 20, 30]
    print(merge_lists_to_dictionary(keys, values))  # Output: {'x': 10, 'y': 20, 'z': 30}