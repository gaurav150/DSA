keys = {'1':'','2': 'abc','3': 'def','4': 'ghi','5': 'jkl',
    '6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz','0': ' ',
    '*': '+', '#': '#'}


def return_all_words(input_number_as_string):
    if len(input_number_as_string) == 0:
        return ['']
    
    ans  = []
    first_char = input_number_as_string[0]
    remaining_string = input_number_as_string[1:]
    keys_for_first_char = keys[first_char]
    words_for_remaining_string = return_all_words(remaining_string)
    
    for char in keys_for_first_char:
          for word in words_for_remaining_string:        
            ans.append(char + word)
    return ans

# Example usage
if __name__ == "__main__":
    input_number = "23"
    print(f"All words for the number '{input_number}':")
    words = return_all_words(input_number)
    for word in words:
        print(word)
    print(f"Total words: {len(words)}")
    print(f"Words: {words}")
    # Output:
    # All words for the number '23':
    # ad
    # ae
    # af
    # bd
    # be
    # bf
    # cd
    # ce
    # cf