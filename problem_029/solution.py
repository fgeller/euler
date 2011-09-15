import time

def run():
    terms = set()
    for base in range(2,101):
        for exp in range(2,101):
            terms.add(pow(base, exp))
    print "%s distinct terms" % len(terms)

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
