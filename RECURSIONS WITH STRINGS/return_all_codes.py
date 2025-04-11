def get_characters_for_digit(value):
    if value <= 0 or  value>26:
        return ""
    return chr(value + 96 -1)

def return_all_codes(input):
    if len(input) == 0: # Base Case
        return ['']
    if len(input) == 1:
        single_char = get_characters_for_digit(int(input))
        return [single_char]
    
    single_digit = int(input[0])
    doubleDigit = int(input[0:2])
    mainAns = []

    ansWithoutFirstDigit = return_all_codes(input[1:])
    for char in ansWithoutFirstDigit:
        mainAns.append(get_characters_for_digit(single_digit) + char)

    if doubleDigit >= 10 and doubleDigit <= 26:
        ansWithoutFirstTwoDigits = return_all_codes(input[2:])
        for char in ansWithoutFirstTwoDigits:
            mainAns.append(get_characters_for_digit(doubleDigit) + char)
    
    return mainAns
                

ans = return_all_codes("1234")
print(ans)