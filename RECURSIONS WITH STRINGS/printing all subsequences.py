'''
printing all subsequences of a string
using recursion
'''

def print_all_indices(string, index, ans):
    # Base case: if the index is equal to the length of the string, print the current subsequence
    if index == len(string):
        print("".join(ans))
        return
    
    # Include the current character in the subsequence
    ans.append(string[index])
    print_all_indices(string, index + 1, ans)
    
    # Exclude the current character from the subsequence
    ans.pop()
    print_all_indices(string, index + 1, ans)


def print_squences(string):
    # Initialize an empty list to store the current subsequence
    ans = []
    print_all_indices(string, 0, ans)


if __name__ == "__main__":
    string = "abc"
    print(f"All subsequences of '{string}':")
    print_squences(string)
    # Output:
    # All subsequences of 'abc':
    # abc
    # ab
    # ac
    # a
    # bc
    # b
    # c
    #