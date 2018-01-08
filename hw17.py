def solve_quadratic_equation(a, b, c): #returns 2 values: either 2 roots, 1 root and none, 2 Nones
    D = b*b - 4*a*c
    if D > 0:
        return ((-b + D**0.5)/ (2*a), (-b - D**0.5)/ (2*a))
    elif D == 0:
        return (-b / (2*a), None)
    else:
        return None, None

a=10
b=2
c=0

print(solve_quadratic_equation(a, b, c))