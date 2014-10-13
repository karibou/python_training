# -*- coding: iso-8859-1 -*-
"""
On dispose d'un tableau bidimensionnel I de taille 10 × 10 et on souhaite calculer le tableau I2
en utilisant la transformation suivante :
I2[i,j] = 0.25 * (I[i-1, j] + I[i+1, j] + I[i, j-1] + I[i, j+1]
"""

import numpy as np


if __name__ == '__main__':
    I1 = np.random.randn(10,10)

    ## size 8x8
    # I2 = np.zeros((8,8))
    I2 = 0.25 * ( I1[0:-2,1:-1] + I1[2:,1:-1] + I1[1:-1,0:-2] + I1[1:-1,2:])
    print I2
    
    ## for a size 10x10
    I3 = np.zeros_like(I1)
    I3[1:-1,1:-1] = 0.25 * (I1[0:-2, 1:-1]
                          + I1[2:,   1:-1]
                          + I1[1:-1, 0:-2]
                          + I1[1:-1, 2:  ])
    print I3
