"""Profiling de fact + version C"""

import sys
import time
from operator import mul

import cfact


def fact1(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def fact2(n):
    res = 1
    for i in xrange(1, n+1):
        res *= i
    return res

def fact3(n):
    if n <= 1:
        return 1
    return reduce(mul, range(1, n+1))

def fact4(n):
    if n <= 1:
        return 1
    return reduce(mul, xrange(1, n+1))


def bench(n):
    latest_res = None
    for fact in (fact1, fact2, fact3, fact4, cfact.fact):
        start = time.time()
        res = fact(n)
        end = time.time()
        print "%s() : %s" % (fact.__name__, end-start)
        if latest_res is not None:
            assert res == latest_res, '%s != %s' % (res, latest_res)
        latest_res = res


if __name__ == '__main__':
    bench(int(sys.argv[1]))
