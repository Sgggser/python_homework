

lst = [-5, 3, 4]
print(lst)
length = len(lst)
lst1 = [abs(lst[i]) for i in range(length)]

maxim = max(lst1)
lst2 = [lst[i]/maxim for i in range(length)]
print(lst2)