import time


def primes(limit):
    nums = range(0, limit)
    nums[0] = None
    nums[1] = None
    cur = 2
    while cur < limit:
        if nums[cur]:
            for multiple in range(2 * cur, limit, cur):
                nums[multiple] = None
        cur += 1
    return [num for num in nums if num]


def run():
    prs = dict()
    for pri in primes(100000):
        prs[pri] = True
    maxn = 0
    maxa = 0
    maxb = 0
    maxfail = 0
    for acoef in range(-999, 1000):
        for bcoef in range(-999, 1000):
            for num in xrange(1, 1000):
                rlt = (num * num) + (acoef * num) + bcoef
                if not(rlt in prs):
                    if maxfail < rlt:
                        maxfail = rlt
                    break
                elif maxn < num:
                    maxn = num
                    maxa = acoef
                    maxb = bcoef
    print "maxfail: %s" % maxfail
    print "maxn %s. maxa %s * maxb %s = %s" % (maxn, maxa, maxb, maxa * maxb)


if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
