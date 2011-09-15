import time

# upper limit: 6 * pow(9,5) < 999 999

def run():
    exp = 5
    finds = []
    sums = dict()
    for ndigs in range(0, 6):
        newsums = []
        for num in range(1, 10):
            numsum = pow(num, exp)
            curnum = num * pow(10, ndigs)
            newsums.append((curnum, numsum))
            for restnum, restsum in sums.items():
                newnum = curnum + restnum
                newsum = numsum + restsum
                newsums.append((newnum, newsum))
                if newnum == newsum: finds.append(newnum)
        for nnum, nsum in newsums: sums[nnum] = nsum

    print "Found %s for exp %s. Their sum is %s." % (finds, exp, sum(finds))

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
