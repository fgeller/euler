def fibSum():
    sum = 0
    # Fibonacci sequence begins with a=0 and b=1
    a, b = 0, 1
    while b < 4000000:
        a, b = b, a+b
        if b % 2 == 0:
            sum += b
    print sum
