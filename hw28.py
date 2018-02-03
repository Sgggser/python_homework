

def encode(str_to_encode, encr_table): # returns enсoded string
    new_string = str_to_encode.lower()
    length = len(encr_table)
    for letter in new_string:
        if letter in encr_table:
            idx = encr_table.index(letter) + 5
            if idx >= length:
                idx -= length
            new_letter = encr_table[idx]
        else:
            new_letter = letter
        new_string = new_string.replace(letter, new_letter)

    return new_string


str_to_encode = input('Введите строку:')
encr_table = [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(10)]

print(encode(str_to_encode, encr_table))

