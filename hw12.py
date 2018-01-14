def sum_of_digits(number): #returns int
    return number // 100 + (number % 100) // 10 + number - (number // 100)*100 - ((number % 100) // 10)*10
