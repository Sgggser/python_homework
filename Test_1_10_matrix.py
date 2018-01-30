import random

def pretty_print_matrix(matrix):
    print()
    for row in matrix:
        for elem in row:
            print('%d' % elem, end='\t')
        print()


def saddle(matrix, m, n): # returns boolean (True- if element(m,n) - saddle point
    matr_rows = len(matrix)
    matr_columns = len(matrix[0])
    is_min_in_row = False
    is_max_in_column = False
    for i in range(matr_rows):
        if (i == m) and min(matrix[i]) == matrix[m][n]:
            is_min_in_row = True
    # Rebuild matrix
    matrix2 = []
    for j in range(matr_columns):
        column = []
        for i in range(matr_rows):
            column.append(matrix[i][j])
        matrix2.append(column)
        if (j == n) and max(matrix2[j]) == matrix[m][n]:
            is_max_in_column = True

    return is_min_in_row and is_max_in_column

matrix = [[3, 8, 7], [5, 9, 6], [2, 6, 7]]
pretty_print_matrix(matrix)
saddle_list = []
for i in range(3):
    for ii in range(3):
        if saddle(matrix, i, ii):
            saddle_list.append([i, ii])
print(saddle_list)
