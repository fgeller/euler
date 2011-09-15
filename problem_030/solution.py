import time

# upper limit: 6 * pow(9,5) < 999 999

def run():
    exp, finds, sums = 5, [], []
    for ndigs in range(0, 6):
        newsums = []
        for num in range(1, 10):
            nsum, cnum = pow(num, exp), num * pow(10, ndigs)
            newsums.append((cnum, nsum))
            ntpls = [(cnum + rnm, nsum + rsm) for rnm, rsm in sums]
            newsums.extend(ntpls)
            for nnm, nsm in ntpls:
                if nnm == nsm: finds.append(nnm)
        sums.extend(newsums)

    print "Found %s for exp %s. Their sum is %s." % (finds, exp, sum(finds))

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
