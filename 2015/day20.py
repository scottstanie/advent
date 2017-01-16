import math
min_presents = 29000000


def present_count(house_num):
    return 10 * sum(factors(house_num))


def present_count2(house_num):
    return 11 * sum(factors_part_2(house_num))

# SLOW :(
# def factors(num):
#     factors = [d for d in range(1, 1 + (num / 2)) if num % d == 0]
#     return factors + [num]


def factors(n):
    '''The faster way'''
    return set(reduce(list.__add__,
               ([i, n / i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def factors_part_2(n):
    '''50 houses means you can start at numbers that are n/50'''
    return (f for f in factors(n) if f >= math.ceil(n / 50))


for i in xrange(100000, 100000000):
    # if present_count(i) >= min_presents:
    if present_count2(i) >= min_presents:
        print i
        break
    if i % 100000 == 0:
        print "Ran through house number %s" % i
        print "%s presents, not yet %s" % (present_count2(i), min_presents)
