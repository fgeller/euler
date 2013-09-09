# # Problem 10 - Summation of primes

UNMARKED = 0
MARKED = 1
FIRST_PRIME = 2

def sum_of_primes(limit=2000000):
    numbers = [UNMARKED] * limit
    number = FIRST_PRIME
    sum = 0

    while number < limit:
        if numbers[number] == UNMARKED:
            sum += number
            numbers = mark_numbers(numbers, number)
        number += 1

    return sum

def mark_numbers(numbers, prime):
    number = prime * 2

    while number < len(numbers):
        numbers[number] = MARKED
        number += prime

    return numbers
    

print sum_of_primes()

