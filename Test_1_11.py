import random

def pretty_print_matrix(matrix):
    print()
    for row in matrix:
        for elem in row:
            print('%d' % elem, end='\t')
        print()


col = 10
row = 15

z=[[random.randint(0,50) for _ in range(col)] for _ in range(row)]

pretty_print_matrix(z)

for i in range(row):
    z[i].sort(reverse= (i % 2 == 0))
pretty_print_matrix(z)
