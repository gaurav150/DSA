def count_zoos(word):
    words = word.strip()
    z_count = words.count('z')
    o_count = words.count('o')

    if 2 * z_count == o_count:
        print("Yes")
    else:
        print("No")


# Example 


count_zoos('zzzoooooo')
count_zoos('zzzzzzzzzzooooooooooooo')