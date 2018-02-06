import string


def encode(str_to_encode): # returns enсoded string
    encr_table = string.ascii_lowercase + string.digits
    length = len(encr_table)
    new_string = ''
    for letter in str_to_encode.lower():
        if letter not in encr_table:
            new_string += letter
        else:
            new_string += encr_table[(encr_table.index(letter) + 5) % length]
    return new_string


str_to_encode = input('Введите строку:')

print(encode(str_to_encode))

