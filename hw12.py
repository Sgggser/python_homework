def sum_of_digits(number): #returns int
    sotni = number // 100
    desjatki = (number % 100) // 10
    edinitsy = number - sotni*100 - desjatki*10
    return sotni + desjatki + edinitsy

test = 120

print(sum_of_digits(test))