

def group_by_surname(list_of_enrollees): # returns 4 ints

    group_1 = 0
    group_2 = 0
    group_3 = 0
    group_4 = 0

    for i in range(len(list_of_enrollees)):
        first_letter = list_of_enrollees[i].split(' ')[1][0]
        if first_letter in 'ABCDEFGHI':
            group_1 += 1
        elif first_letter in 'JKLMNOP':
            group_2 += 1
        elif first_letter in 'QRST':
            group_3 += 1
        elif first_letter in 'UVWXYZ':
            group_4 += 1
    return (group_1, group_2, group_3, group_4)


print(group_by_surname(['Will Smith', 'Jay Z']))