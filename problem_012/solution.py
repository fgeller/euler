# Problem 12: Highly divisible triangular number
#
# http://stackoverflow.com/questions/110344/algorithm-to-calculate-the-number-of-divisors-of-a-given-number
# n = a^x * b^y * c^z
# number_of_divisors = (x + 1) * (y + 1) * (z + 1)

def get_sum(number):
    return number * (number + 1) / 2

def get_number_of_divisors(number):
    prime_factors = {}
    divisor = 2

    while (divisor <=  number):
        if ((number % divisor) == 0):
            if not divisor in prime_factors:
                prime_factors[divisor] = 1
            prime_factors[divisor] += 1
            number = number/divisor
        else:
            divisor += 1

    count = 1
    for value in prime_factors.values():
        count *= value

    return count


def get_highly_divisible_triangular_number(number_of_divisors):
    number = 0
    count = 0
    while (count <= number_of_divisors ):
        number += 1
        count = get_number_of_divisors(get_sum(number))

    return get_sum(number)

print get_highly_divisible_triangular_number(500)
