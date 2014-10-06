#!/usr/bin/python

list3 = [(1,6), (2,7), (3,8), (4,9), (5,10)]

list1 = [i for (i,b) in list3]
list2 = [j for (a,j) in list3]

assert list1 == [1, 2, 3, 4, 5]
assert list2 == [6, 7, 8, 9, 10]

#
# ou bien
#
list1 = []
list2 = []

for i,j in list3:
	list1.append(i)
	list2.append(j)

assert list1 == [1, 2, 3, 4, 5]
assert list2 == [6, 7, 8, 9, 10]
