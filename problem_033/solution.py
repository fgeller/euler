import time
from fractions import Fraction as F


def istrivial(numer, denom):
    if denom % 10 == 0 or denom / 10 != numer % 10: return False
    return float(numer / 10) / (denom % 10) == float(numer) / denom


def run():
    fracs = []
    for numer in range(11, 100):
        for denom in range(numer + 1, 100):
            if istrivial(numer, denom):
                fracs.append(F(numer, denom))
    print "Simplified product of trivial fractions: %s"\
        % reduce(lambda mem, obj: mem * obj, fracs)

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
