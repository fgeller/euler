from decimal import Decimal as D
from decimal import getcontext
import time


def run():
    prec = 2000
    getcontext().prec = prec
    maxlen = 0
    maxden = 0
    fracs = [((D(1) / D(den)).as_tuple().digits, den) for den in range(3, 1000, 2)]
    for frac, den in fracs:
        clen = 1
        while clen < prec / 2:
            if frac[0:clen] == frac[clen:(2 * clen)]:
                if clen > maxlen:
                    maxlen = clen
                    maxden = den
                break
            else: clen += 1

    print "Max cycle length %s found for d=%s." % (maxlen, maxden)

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
