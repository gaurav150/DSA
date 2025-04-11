''' 
using recursion to print all permutations of a string
'''
def print_permutations(string,takensofar):
    if len(string) == 0:
        print(takensofar)
        return
    
    first_char = string[0]
    remaining_string = string[1:]
    for i in range(len(takensofar)+1):
        new_permutation = takensofar[:i] + first_char + takensofar[i:]
        print_permutations(remaining_string, new_permutation)
    return

# Example usage
if __name__ == "__main__":
    string = "abc"
    print(f"All permutations of '{string}':")
    print_permutations(string, "")
    # Output:
    # All permutations of 'abc':
    # abc
    # acb
    # bac
    # bca
    # cab
    # cba


