import random
import string


def generate_password(NUMBER_OF_SYMBOLS=8):
    using_symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits + '_'

    while True:
        password = ''
        use_lowercase = False
        use_uppercase = False
        use_digits = False
        for _ in range(NUMBER_OF_SYMBOLS):
            add_symbol = using_symbols[random.randint(1, len(using_symbols)-1)]
            if add_symbol in string.ascii_lowercase:
                use_lowercase = True
            elif add_symbol in string.ascii_uppercase:
                use_uppercase = True
            elif add_symbol in string.digits:
                use_digits = True
            password += add_symbol
        if use_lowercase and use_uppercase and use_digits:
            return password


# for _ in range(100):
#     print(generate_password())