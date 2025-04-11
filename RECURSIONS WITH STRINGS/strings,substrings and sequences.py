'''
String
Substring
Subsequence
'''
def return_subsequences(string):
    '''
    return all subsequences of a string using recursion
    '''
    if not string:
        ans = [""]
        return ans
    ans = []
    
    first_char = string[0]
    small_ans = return_subsequences(string[1:])
    ans.extend(small_ans)
    
    for eachpermutation in small_ans:
        ans.append(first_char + eachpermutation)
    return ans 
        

if __name__ == "__main__":
    string = "abc"
    subsequences = return_subsequences(string)
    print(f"All subsequences of '{string}': {subsequences}")
    # Output:
    # All subsequences of 'abc': ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']