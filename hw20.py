import random

def diff_even_odd(num_limit, lower_bound, upper_bound): #returns int
    sum_even = 0 #сумма четных
    sum_odd = 0 #сумма нечетных
    counter = 0
    while counter < num_limit:
        counter += 1
        rand_num = random.randint(lower_bound,upper_bound)
        if rand_num % 2 == 0:
            sum_even += rand_num
        else:
            sum_odd += rand_num
        print(counter, rand_num, sum_even, sum_odd)
    return sum_even - sum_odd


sum_diff = diff_even_odd(100, 0, 100)
print()
print('--------------------')
print()
print(sum_diff)