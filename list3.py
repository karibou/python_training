#!/usr/bin/python


list1 = ['a','b','c','d']
list2 = [(0, 'a'),(1,'b'), (2,'c'), (3,'d')]
list2d = []

for (index, element) in enumerate(list1):
	list2d.append((index,element))

assert list2d == list2, list2d

print "list2d : %s" %list2d

#
# ou bien
#
list2d=[]

for t in enumerate(list1):
	list2d.append(t)

assert list2d == list2, list2d

print "list2d : %s" %list2d
