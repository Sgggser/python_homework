def power(base, exp):
    print('power func')
    return base**exp

result1 = power(3, 2)
print(result1)
pi = 3.14


def print_delimeter(symbol='+', num_repeat=40):
    print(symbol*num_repeat)


def pretty_print(value):
    print_delimeter('`', 45)
    print('Value:', value)
    print_delimeter()


def rectangle_square(width, height):
    result = width * height
    return result


def circle_square(radius):
    result = power(radius, 2)*pi
    return result


def calc_sum_and_product(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result


result2 = rectangle_square(10, 20)
pretty_print(result2)
result3 = circle_square(10)
pretty_print(result3)

res4, res5 = calc_sum_and_product(2, 3)
pretty_print(res4)
pretty_print(res5)

#comment

result6 = pretty_print(42)
print(result6, type(result6))

def faren2celc(degrees):
    return (degrees - 32) / 1.8

def cels2far(degrees):
    return (degrees*1.8 + 32)

print(cels2far(37))
