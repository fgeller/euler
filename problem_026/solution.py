from decimal import Decimal as D
from decimal import getcontext
import time

PRECISION = 10000
DENOM_TO_CLEN = dict()


def test(frac, den, pfx):
    clen = 1
    while clen < (PRECISION - pfx) / 2:
        tfrac = frac[pfx:pfx + clen]
        if tfrac == frac[pfx + clen:pfx + (2 * clen)]:
            # I had a test here that would verify the next x segments,
            # to make sure it is less likely to be a false positive,
            # but it doesn't seem necessary
            DENOM_TO_CLEN[den] = clen, frac[0:clen]
            return True
        else: clen += 1

    return False


def run():
    start = time.time()
    getcontext().prec = PRECISION
    fracs = [((D(1) / D(den)).as_tuple().digits, den) for den in range(3, 1000, 2)]
    longfracs = [(frac, den) for frac, den in fracs if len(frac) == PRECISION]
    for frac, den in longfracs:
        pfx = 0
        while pfx < PRECISION:
            if test(frac, den, pfx): break
            else: pfx += 1

    print "Concluded search for cycles, looking for max length."
    mlen = 1
    mden = None
    for (den, (clen, frac)) in DENOM_TO_CLEN.items():
        if mlen < clen:
            mlen = clen
            mden = den

    end = time.time()
    etime = round(end - start)
    print "Max cycle length found: %s for d=%s in %ss" % (mlen, mden, etime)
    print "Cycle: %s " % ''.join([str(num) for num in DENOM_TO_CLEN[mden][1]])

if __name__ == '__main__':
    run()
