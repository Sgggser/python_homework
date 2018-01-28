
str_number = input('Введите пятизначное число ')
if len(str_number) != 5 or not str_number.isnumeric():
    print ('Неверный ввод 5-тизначного числа')
else:
    number = int(str_number)
    print(number)
    product = int(str_number[0]) * int(str_number[2]) * int(str_number[4])
    print('Произведение нечетных цифр = ', product)