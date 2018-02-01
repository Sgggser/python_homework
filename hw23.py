import random

rand_num = random.randint(1, 10)
print('Загаданное число:', rand_num)
guess_num = 0
while (guess_num != rand_num):
    guess_num = int(input('Guess the number? '))
    if guess_num > rand_num:
        print('Ваш ответ больше загаданного числа')
    elif guess_num < rand_num:
        print('Ваш ответ меньше загаданного числа')
