import time
from math import factorial as fac


def run():
    facs = [fac(num) for num in range(0, 10)]
    curiousnums = []
    for num in range(10, 1000000):
        cnum, nsum = num, 0
        while cnum > 0 and nsum < num:
            nsum += facs[cnum % 10]
            cnum /= 10
        if nsum == num and cnum == 0:
            curiousnums.append(num)
    print curiousnums
    print "The curious nums sum up to %s." % sum(curiousnums)

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
