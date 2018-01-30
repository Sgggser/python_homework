
lst = [1, 2, 30, 4, 50]
print(lst)
max_elem = max(lst)
min_elem = min(lst)
max_idx = lst.index(max_elem)
min_idx = lst.index(min_elem)

lst[max_idx], lst[min_idx] = lst[min_idx], lst[max_idx]
print(lst)
