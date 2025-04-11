'''
return permutations of a string
using recursion to print all permutations of a string as a list
'''

def permutations(s):
    """
    Function to generate all permutations of a string using recursion.
    
    Parameters:
    s (str): The string to generate permutations from.
    
    Returns:
    list of str: A list containing all permutations of the string.
    """
    # Your code here
    if len(s) == 0:
        return ['']
        
    first_char = s[0]
    permutation_small = permutations(s[1:])
    all_permutations = []
    for perm in permutation_small:
        for i in range(len(perm)+1):
            all_permutations.append(perm[0:i]+first_char+perm[i:])
            
    return all_permutations

# Example usage
if __name__ == "__main__":
    string = "abc"
    print(f"All permutations of '{string}':")
    permut = permutations(string)
    for perm in permut:
        print(perm)
    print(f"Total permutations: {len(permut)}")
    print(f"Permutations: {permut}")
    # Output:
    # All permutations of 'abc':
    # abc
    # acb
    # bac
    # bca
    # cab
    # cba