def triangle_square_and_perimeter(a, b): #returns 2 values
    square = a*b / 2
    perimeter = a + b + (a*a + b*b)**0.5
    return square, perimeter

kat1 = 2
kat2 = 3
print(triangle_square_and_perimeter(kat1, kat2))