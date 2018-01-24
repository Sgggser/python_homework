import random

def get_max_digit(number): # returns int
    number_str = str(number)
    print(number_str)
    length = len(number_str)
    print(length)
    lst = [number_str[i] for i in range(length)]
    print(lst)
    return int(max(lst))

number = random.randint(10 ** 11, 10 **12)
print(get_max_digit(number))