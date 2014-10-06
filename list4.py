#!/usr/bin/python

list1 = range(1,6)
list2 = range(6,11)

list3 = zip(list1,list2)

assert list3 == [(1,6), (2,7), (3,8), (4,9), (5,10)], list3
