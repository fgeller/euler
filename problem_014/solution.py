def longest_collatz_sequence(limit):

    max = 0, 0

    for i in xrange(limit):
        sequenceCount = calculate_collatz_sequence(i)
        if sequenceCount > max[1]:
            max = i, sequenceCount

    return max


def calculate_collatz_sequence(number, counter = 1):

    if number == 1:
        return counter
    elif number == 0:
        return 1
    else:
        if number % 2 == 0:
            return calculate_collatz_sequence(number/2, counter + 1)
        else:
            return calculate_collatz_sequence(3*number + 1, counter + 1)


print longest_collatz_sequence(100)

                

