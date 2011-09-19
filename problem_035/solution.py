import time


def primeflags(upperlimit):
    nums = [num for num in range(0, upperlimit)]
    nums[0] = None
    nums[1] = None
    low = 2
    while low < upperlimit / 2:
        if nums[low]:
            for mul in [num for num in range(low * 2, upperlimit, low)]:
                nums[mul] = None
        low += 1
    return nums


def rotations(num):
    rots = []
    strnum = str(num)
    for _ in range(1, len(strnum)):  # don't include self
        strnum = strnum[1:] + strnum[0]
        rots.append(int(strnum))
    return rots


def run():
    limit = 1000000
    circularprimes = []
    isprime = primeflags(limit)
    primes = [prim for prim in isprime if prim]
    for prim in primes:
        flag = True
        for primrot in rotations(prim):
            if not(isprime[primrot]):
                flag = False
                break
        if flag: circularprimes.append(prim)

    print "There are %s circular primes below %s"\
        % (len(circularprimes), limit)

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
