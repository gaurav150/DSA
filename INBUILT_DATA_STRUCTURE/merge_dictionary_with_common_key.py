'''
Merge Dictionaries with Overlapping Keys

Design a Python function named merge_dicts_with_overlapping_keys
 that merges multiple dictionaries into a single dictionary. 
 If a key appears in more than one dictionary, sum up their values.

Parameters:

dicts (list): A list of dictionaries where keys might overlap.

Returns:

A single dictionary where values for overlapping keys are summed.
'''

def merge_dicts_with_overlapping_keys(dicts):
    merged_dict = {}
    if len(dicts) == 0:
        return merged_dict
    for ele in dicts:
        for key,value in ele.items():
            if key in merged_dict:
                merged_dict[key] += value
            else:
                merged_dict[key] = value
    return merged_dict

# Example usage:
dicts = [
    {'a': 1, 'b': 2},
    {'b': 3, 'c': 4},
    {'a': 5, 'd': 6}
]   