#!/usr/bin/env python
LIMIT = 28123


def is_abundant(some_num):
    div_sum = 0
    for possible_div in range(2, (some_num / 2) + 1):
        if some_num % possible_div == 0:
            div_sum += possible_div
            if div_sum > some_num:
                return True
    return False


def abundant_numbers(upper):
    return [some_num for some_num in range(1, upper) if is_abundant(some_num)]


anums = abundant_numbers(LIMIT)
print "Nr. of abundant_numbers: %s" % len(anums)

sums_of_anums = set()

for anum1 in anums:
    for anum2 in anums:
        sums_of_anums.add(anum1 + anum2)

all_nums = range(1, 28124)

our_nums = [num for num in range(1, 28124) if not(num in sums_of_anums)]

print "sum: %s" % sum(our_nums)
