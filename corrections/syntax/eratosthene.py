"""Eratosthene's sieve"""

import math

# solution 1

def prime(n):
    crible = range(n+1)
    crible[0] = None # 0 is not prime
    crible[1] = None # 1 is not prime

    stop = math.floor(math.sqrt(n)) # trick: don't go after sqrt(N)

    for a in crible:
        if a > stop:
            break
        if a is not None:
            # a is prime
            for r in xrange(a*2, n+1, a):
                crible[r] = None

    return [a for a in crible if a is not None]

# solution 2

def prime2(n):
    crible = range(n+1)
    crible[0] = None # 0 is not prime
    crible[1] = None # 1 is not prime

    for i in xrange(2, int(math.ceil(math.sqrt(n)))):
        a = crible[i]
        if a is not None:
            for r in xrange(a*2, n+1, a):
                crible[r] = None

    return [a for a in crible if a is not None]

print prime(50)
assert prime2(50) == prime(50)
