# -*- coding: utf-8 -*-
"""Make two simple arrays with NumPy.

make_simple_array.py

Python Numpy Intro.
"""

from pprint import pprint
import numpy as np

# Exercises : Create the following array with the simplest solution:


def createA():
    """Create the first array."""
    a = np.ones((4, 4))
    a[2, 3] = 2.
    a[3, 1] = 6.
    return a


def createB():
    """Create the second array."""
    b = np.zeros((6, 5))
    b[1:,:] += np.diag(np.arange(2.,7.))
    return b


def createB2():
    """Other solution for B: diagonal matrix"""
    b = np.diag(np.arange(2.,7.), k=-1)
    return b[:,:-1]


if __name__ == '__main__':
    a = createA()
    print('A: ')
    pprint(a)

# [[ 1.  1.  1.  1.]
#  [ 1.  1.  1.  1.]
#  [ 1.  1.  1.  2.]
#  [ 1.  6.  1.  1.]]

    b = createB()
    print('B: ')
    pprint(b)

# [[ 0.  0.  0.  0.  0.]
#  [ 2.  0.  0.  0.  0.]
#  [ 0.  3.  0.  0.  0.]
#  [ 0.  0.  4.  0.  0.]
#  [ 0.  0.  0.  5.  0.]
#  [ 0.  0.  0.  0.  6.]]

    b = createB2()
    print('B: ')
    pprint(b)

# [[ 0.  0.  0.  0.  0.]
#  [ 2.  0.  0.  0.  0.]
#  [ 0.  3.  0.  0.  0.]
#  [ 0.  0.  4.  0.  0.]
#  [ 0.  0.  0.  5.  0.]
#  [ 0.  0.  0.  0.  6.]]
