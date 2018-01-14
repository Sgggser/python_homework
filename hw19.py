import random

def diff_min_max(num_limit, lower_bound, upper_bound): #returns int
    max_num = lower_bound
    min_num = upper_bound
    for _ in range(num_limit):
        rand_num = random.randint(lower_bound, upper_bound)
        print(rand_num)
        if rand_num < min_num:
            min_num = rand_num
        if rand_num > max_num:
            max_num = rand_num
    print('------------')
    return(max_num - min_num)

print(diff_min_max(10, 1, 50))