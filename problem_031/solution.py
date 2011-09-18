import time


def split_opts(amt, coins):
    if amt == 0:
        return 1
    elif amt < 0 or not(coins):
        return 0
    else:
        return split_opts(amt, coins[1:]) + split_opts(amt - coins[0], coins)


def run():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    amt = 200
    print "There are %s options to split %s."\
        % (split_opts(amt, coins), amt)

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
