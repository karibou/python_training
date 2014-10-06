#!/usr/bin/python

d = {'a':1, 'b':2, 'c':3}

d2 = {}

for key, item in d.items():
	d2[item]=key

assert d2 == {1:'a', 2:'b', 3:'c'}, 'pas bon %s' % d2
