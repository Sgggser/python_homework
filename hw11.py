import math

def degrees2radians(degrees): #returns float
    return degrees*math.pi/180

grad1=60
grad2=45
grad3=40

radian1=degrees2radians(grad1)
radian2=degrees2radians(grad2)
radian3=degrees2radians(grad3)

print(radian1, radian2, radian3)

print(math.cos(radian1), math.cos(radian2), math.cos(radian3))
