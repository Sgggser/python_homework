
lst = [1, 2, 30, 4, 50]
print(lst)
ma = max(lst)
mi = min(lst)
ma_ind = lst.index(ma)
mi_ind = lst.index(mi)

lst[ma_ind], lst[mi_ind] = lst[mi_ind], lst[ma_ind]
print(lst)
