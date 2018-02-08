


def gen_primes(): # returns list of ints
    list_of_primes = [1, 2]
    for i in range(3, 101):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
        if prime:
            list_of_primes.append(i)
    return list_of_primes


print(gen_primes())
