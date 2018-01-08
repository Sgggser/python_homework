import random

for i in range (5):
    if i % 2 == 0:
        print('hello world', i)
    else:
        print('happy new year', i)

for i in range(20, 10, -2):
    print('iteration#:', i)


for _ in range(10):
    print('hello world')

print('-----------------------')
for char in "abc":
    print(char)

for weekday in ('Mo', 'Tu', 'We', 'Thu', 'Fri', 'Sat', 'Sun'):
    print(weekday)


for i in range(2, 101, 2):
    print(i)

sum_total = 0
for i in range(1, 101):
    sum_total = sum_total + i
print(sum_total)

def sum_of_n(n):
    sum_total = 0
    for i in range(1, n+1):
        sum_total += i
    return sum_total

print(sum_of_n(100))

t = 'Вы перешли в режим инкогнито.'
print(len(t.split(' '))-1)
print(t.count(' '))

def find_num_of_uppers(text):
    upper_total = 0
    for char in text:
        if char.isupper():
            upper_total += 1
    return upper_total

print(find_num_of_uppers(t))

def camelize_me(var_name):
    var_name_lst = var_name.split('_')
    result = ''
    print(var_name_lst)
    for part_name in var_name_lst:
        #print(part_name, part_name.capitalize())
        result += part_name.capitalize()
    return result

print(camelize_me('emploee_first_name'))
print(camelize_me('d_ve_venei_cwicwu_v'))
print(camelize_me('em'))

def avr_whatever_of_n(n, lower_bound, upper_bound):
    rand_total = 0
    for _ in range(n):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)
        rand_total += rand_num
    avr_rand = rand_total / n
    return avr_rand


print('%.2f' % avr_whatever_of_n(11, 100, 200))