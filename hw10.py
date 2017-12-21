

s1 = 'Leo Tolstoy*1828-08-28*1910-11-20'
s2 = 'Marcus Aurelius*121-04-26*180-03-17'
s = s2

s_splitted = s.split('*')
print(s_splitted[0])

date_born = s_splitted[1]
date_passedaway = s_splitted[2]

date_born_splitted = date_born.split('-')
date_passedaway_splitted = date_passedaway.split('-')

age = int(date_passedaway_splitted[0]) - int(date_born_splitted[0])
print(age)
