def findSum(limit = 1000):
    sum = 0
    for number in range(3, limit):
        if number % 3 == 0:
                sum += number
                continue
        if number % 5 == 0:
                sum += number
    print sum
