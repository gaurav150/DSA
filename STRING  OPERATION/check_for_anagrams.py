def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    
    s= s.replace(" ", "").lower()
    t= t.replace(" ", "").lower()
    if len(s) != len(t):
        return False
    s_count = {}
    t_count = {}
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1
    return s_count == t_count

# Example usage:
if __name__ == "__main__":
    str1 = "Listen"
    str2 = "Silent"
    print(f"Are '{str1}' and '{str2}' anagrams? {is_anagram(str1, str2)}")
    
    str1 = "Hello"
    str2 = "World"
    print(f"Are '{str1}' and '{str2}' anagrams? {is_anagram(str1, str2)}")
    
    str1 = "Astronomer"
    str2 = "Moon starer"
    print(f"Are '{str1}' and '{str2}' anagrams? {is_anagram(str1, str2)}")