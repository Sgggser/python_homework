s = 'Mark Zuckerberg'
print(s)

name_splitted = s.split(' ')
s1 = name_splitted[0]
s2 = name_splitted[1]

s1, s2 = s2, s1
print(s1, s2)