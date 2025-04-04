def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    left,right=0,len(letters)-1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return letters[left % len(letters)]

# Example usage

if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "a"
    result = next_greatest_letter(letters, target)
    print("The smallest letter greater than target is:", result)  # Output: "c"