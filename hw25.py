import random

def shuffle_list(list_to_shuf): # no return (shuffles list in place)
    for _ in range(200):
        idx_1 = random.randint(0, 49)
        idx_2 = random.randint(0, 49)
        list_to_shuf[idx_1], list_to_shuf[idx_2] = list_to_shuf[idx_2], list_to_shuf[idx_1]
    pass

list_odd_num = [i for i in range(1, 100) if i % 2 == 1]
print(list_odd_num)
shuffle_list(list_odd_num)
print(list_odd_num)
