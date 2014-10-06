#!/usr/bin/python

l = ['toto','tata','tutu']

l2 = []
for i in l:
	if 'o' in i:
		l2.append(i)

print l2

l3 = [ i for i in l if 'o' in i]

print l3
