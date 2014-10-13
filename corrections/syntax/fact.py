
def fact1(n):
    """return fact(n), computed recursivly"""
    assert n >= 0
    if n == 0:
        return 1
    return n * fact1(n-1)


def fact2(n):
    """return fact(n), computed without recursion"""
    assert n >= 0
    # trick to avoid an iteration: initialize result to n (unless n == 0)
    result = n or 1
    for i in range(2, n):
        result *= i
    return result

import operator
from functools import reduce

def fact3(n):
    """return fact(n), computed without recursion and using builtins functions"""
    assert n >= 0
    if n <= 1:
        return 1
    return reduce(operator.mul, range(1, n+1))

if __name__ == '__main__':
    # tests
    for factf in (fact1, fact2, fact3):
        assert factf(0) == 1
        assert factf(1) == 1
        assert factf(5) == 120

