# -*- coding: iso-8859-1 -*-
"""
"""
import numpy as np
from numpy.random import uniform
import pylab as pl

R = 1.0
# study for -R<w<R and -R<y<R

surf_square = 4. * R**2
#surf_circle = np.pi * R**2

# number of darts hitting the square (= sample size)
N_square = 1e6


def tirage(N_square):
    """
    """
    # Random positions (x,y)
    X = uniform(low=-R, high=R, size=N_square)
    Y = uniform(low=-R, high=R, size=N_square)
    return X, Y


def count_darts_in_circle(X, Y):
    """
    """
    ## sum over booleans work: True=1, False=0
    N_circle = (X**2+Y**2 <= 1).sum()
    
    ## other solution
    N_circle2 = len(np.where(X**2+Y**2 <= 1)[0])

    assert np.alltrue(N_circle == N_circle2)
    ## naive loop
    # N_circle=0
    # for x1,y1 in zip(X,Y):
    #     # condition for hitting the circle: R^2 < 1
    #     if np.sqrt(x1**2+y1**2) <= 1:
    #         N_circle += 1
    return N_circle


def pi_estimate(N_square):
    """
    """
    X, Y = tirage(N_square)
    N_circle = count_darts_in_circle(X, Y)
    # surf_circle / surf_square = pi / 4
    return 4. * N_circle / N_square


def pi_estimate_with_steps(N_square, step = 1):
    """
    """
    pi_array = np.zeros(step)
    ## fill with independant data
    for i in range(step):
        pi_array[i] = pi_estimate(N_square/step)

    ## create average on cumulated data
    pi_array_cumul = np.zeros_like(pi_array)
    for i in range(len(pi_array)):
        pi_array_cumul[i] = pi_array[:i].mean()
    return pi_array_cumul


def plot_error(pi_list):
    """
    """
    error_list = [(value-np.pi)/np.pi for value in pi_list]
    
    pl.plot(range(1, len(error_list)+1), error_list)
    pl.xlabel('step')
    pl.ylabel('relative error')


if __name__ == '__main__':
    print "Estimate for %i darts: %.3f" % (N_square, pi_estimate(N_square))

    ## warning: 1e5 is a float
    pi_array_cumul = pi_estimate_with_steps(N_square, step = int(1e5))
    plot_error(pi_array_cumul.tolist())
    pl.show()
