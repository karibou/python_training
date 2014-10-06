#!/usr/bin/python

prenoms = ['arthur', 'babar', 'celeste']
ages = [ 5, 25, 27 ]
mydict = {}

for index, value in enumerate(prenoms):
	print "{0} {1}".format(index, value)
	mydict[value] = ages[index]

assert mydict == {'arthur': 5, 'babar': 25, 'celeste': 27}, mydict
