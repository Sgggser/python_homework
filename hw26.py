import random

def calc_frequency(lst): # returns the most frequent number or None
    value_list = [-1, 0, 1]
    frequency_list = [lst.count(-1), lst.count(0), lst.count(1)]
    most_frequent_element = value_list[frequency_list.index(max(frequency_list))]
    frequency_list.sort()
    if frequency_list[2] != frequency_list[1]:
        return most_frequent_element
    else:
        return None
    pass


rand_list = [random.randint(-1, 1) for _ in range(11)]
print(rand_list)
print(calc_frequency(rand_list))