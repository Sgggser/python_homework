#for i in range(255):
#    print(i, chr(i))

def sum_symbol_codes(first, last):
    if first > last:
        first, last = last, first
    sum_total = 0
    for i in range(ord(first), ord(last)+1): #returns int
        sum_total += i
    return sum_total

print(sum_symbol_codes('ü', 'þ'))