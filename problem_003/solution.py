# Problem 3 - Largest prime factor

def findLargestPrimeFactor(number=600851475143):

    for factor in xrange(2, number + 1, 1):
        if number % factor == 0 and isPrime(factor):
            if number / factor == 1:
                return factor
            else:
                return findLargestPrimeFactor(number/factor)


def isPrime(number):

    if (number == 2):
        return True

    if (number % 2 == 0):
        return False

    for factor in xrange(3, number/2, 1):
        if number % factor == 0:
            return False

    return True

print findLargestPrimeFactor()
