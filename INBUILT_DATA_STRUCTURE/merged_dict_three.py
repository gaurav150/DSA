def merge_three_dictionaries(dict1, dict2, dict3):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    for key , value in dict2.items():
        merged_dict[key] = value  # Add items from the second dictionary
    for key , value in dict3.items():
        merged_dict[key] = value
    return merged_dict  # Return the merged dictionary

# Example usage:
if __name__ == "__main__":
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    dict3 = {'d': 5, 'e': 6}
    print(merge_three_dictionaries(dict1, dict2, dict3))  
    # Output: {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}

    dict1 = {'x': 10}
    dict2 = {'y': 20}
    dict3 = {'z': 30}
    print(merge_three_dictionaries(dict1, dict2, dict3))  
    # Output: {'x': 10, 'y': 20, 'z': 30}
