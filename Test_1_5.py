def close_to_ten(num):
    return abs(10 - num)


num1 = float(input('Введите первое число '))
num2 = float(input('Введите второе число '))

if close_to_ten(num1) > close_to_ten(num2):
    print(num2)
if close_to_ten(num1) < close_to_ten(num2):
    print(num1)
