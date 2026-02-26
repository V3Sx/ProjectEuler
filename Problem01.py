""" If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

def sum_of_multiples(): #eu tava colocando um parametro aqui, mas não precisava
    total = 0
    for i in range(1, 1000): #define o range aqui mesmo
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total
print(sum_of_multiples())