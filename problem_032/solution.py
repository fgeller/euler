import time


def ispandigital(strid):
    sid = sorted(strid)
    if sid[0] == '0': return False
    for idx in range(1, 9):
        if not(sid[idx - 1] < sid[idx]): return False
    return True


def pandigitalproducts():
    prods = set()
    for leftm in range(1, 99):
        for rightm in range(leftm, 9877):
            product = leftm * rightm
            strid = str(leftm) + str(rightm) + str(product)
            if 9 < len(strid): break
            elif 9 == len(strid):
                if ispandigital(strid):
                    prods.add(product)
    return prods


def run():
    prods = pandigitalproducts()
    print "There are %s pandigital products that sum up to %s."\
        % (len(prods), sum(prods))

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
