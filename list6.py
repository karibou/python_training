#!/usr/bin/python

list1 = range(11,23)

list2 = [i*2 for i in list1]

list3 = [i for i in list1 if i % 2 == 0]

print list1
print list2
print list3
