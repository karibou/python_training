# -*- coding: utf-8 -*-
"""
Read text file and compte some stats.

See files 'introduction_women_percentage.txt' and 'introduction_organisms.txt'.

introduction_women_stat.py

Python Intro Numpy.
"""

import os.path
from pprint import pprint
import numpy as np

WOMEN_STAT_FILENAME = os.path.join(os.path.dirname(__file__), 'input', 'women_percentage.txt')
ORGANISM_FILENAME = os.path.join(os.path.dirname(__file__), 'input', 'organisms.txt')


if __name__ == '__main__':
    # Question 1. Read the first file.
    women = np.loadtxt(WOMEN_STAT_FILENAME)
    print 'Women array shape: ', women.shape
    pprint(women)

    # Question 2. A table with years.
    year = np.arange(2006, 2000, -1)
    pprint(year)

    # Question 3. Read the 2nd file.
    organism = np.loadtxt(ORGANISM_FILENAME, dtype=str)
    pprint(organism)
    print 'organism size: ', organism.size

    # Question 4. Check dimensions.
    print "organism.size == women.shape[0] ?"
    assert(organism.size == women.shape[0])
    print organism.size == women.shape[0]

    # Question 5. Max by year.
    women.max(axis=0)
    # Or
    # for i, line in enumerate(np.transpose(women)):
    #     print year[i], max(line)

    # Question 6. Temporal mean for each organism.
    time_mean = women.mean(axis=1)
    print 'Time average, per institute; ', time_mean

    # Question 7. Max for year 2004.
    index = women[:,2].argmax()
    print 'Max percentage (year 2004) for: ', organism[index]

    # Question 8. What organism has got the max according to time.
    print organism[women.argmax(axis=0)]
