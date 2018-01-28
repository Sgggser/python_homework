def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


sum_fi = 0

for i in range(1, 10+1):
    sum_fi += fibonacci(i)

print(sum_fi)
