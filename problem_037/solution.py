import time


def isinteresting(prime, primes):
    """
    Test whether the given prime number is interesting, i.e.,
    truncatable from left to right and vice versa.
    """
    strprime = str(prime)
    for cut in range(1, len(strprime)):
        if not(int(strprime[:cut]) in primes): return False
        if not(int(strprime[cut:]) in primes): return False

    return True


def genprimes(upperlimit):
    """
    Returns a list of prime numbers
    """
    nums = [num for num in range(0, upperlimit)]
    nums[0] = None
    nums[1] = None
    low = 2
    while low < upperlimit / 2:
        if nums[low]:
            for mul in [num for num in range(low * 2, upperlimit, low)]:
                nums[mul] = None
        low += 1

    return [prim for prim in nums if prim]


def run():
    iprimes = []
    primes = genprimes(1000000)
    for prim in primes[4:]:
        if isinteresting(prim, primes):
            iprimes.append(prim)

    print 'The sum of of %s interesting primes:\n%s\nis %s'\
        % (len(iprimes),
           '\n'.join([str(prim) for prim in iprimes]),
           sum(iprimes))


if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
