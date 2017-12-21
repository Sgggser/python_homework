import math

a = 1
b = 3
c = 5
result = abs(a + b) / (a + b)**3 - math.cos(c)
print('Для значений a=%g b=%g c=%g результат функции: %g' % (a, b, c, result))