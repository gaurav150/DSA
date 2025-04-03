def count_word_frequency(sentence):
    lst = sentence.lower().split()
    
    a_dict = {}
    if not sentence:
        return a_dict
    for ele in lst:
        if ele in a_dict:
            a_dict[ele] += 1
            
        else:
            a_dict[ele] = 1
    
    return a_dict

# Example usage:
sentence = "Hello world hello"
word_frequency = count_word_frequency(sentence)
print(word_frequency)  # Output: {'hello': 2, 'world': 1}