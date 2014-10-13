def prime(n):
    crible = range(n + 1)
    crible[0] = None
    crible[1] = None
    for i in crible:
        if i is not None:
            for j in xrange(2*i, n +1, i):
                crible[j] = None
    return [i for i in crible if i is not None]


assert prime(20) == [2, 3, 5, 7, 11, 13, 17, 19], 'pas bon %s' % prime(20)
