def circles_intersection(x1, y1, r1, x2, y2, r2): #returns boolean
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if dist <= r1 and dist <= r2:
        return dist >= abs(r1 - r2)
    else:
        return dist<= r1 + r2