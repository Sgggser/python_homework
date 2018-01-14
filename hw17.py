def solve_quadratic_equation(a, b, c): #returns 2 values: either 2 roots, 1 root and none, 2 Nones
    discrim = b*b - 4*a*c
    if discrim > 0:
        return ((-b + discrim**0.5)/ (2*a), (-b - discrim**0.5)/ (2*a))
    elif discrim == 0:
        return (-b / (2*a), None)
    else:
        return None, None