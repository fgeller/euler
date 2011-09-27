import time


def int2bin(num):
    """
    Convert the given number to a (max 20-digit) binary

    Arguments:
    - `num`: an int
    """
    digs = ''.join([str((num >> shift) & 1) for shift in range(20, -1, -1)])
    return digs[digs.find('1'):]


def ispalindrom(string):
    """
    Return True if the given string is a palindrom, False otherwise

    Arguments:
    - `string`: A str
    """
    return string == string[::-1]


def run():
    pals = []
    for num in range(1, 1000000):
        strdec = str(num)
        strbin = int2bin(num)
        if ispalindrom(strdec) and ispalindrom(strbin):
            pals.append(num)
    print 'The sum of palindrom base 2 and 10, less than 1000000 is %s'\
        % sum(pals)

if __name__ == '__main__':
    start = time.time()
    run()
    print "%ss elapsed." % round(time.time() - start)
