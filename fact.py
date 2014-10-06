#!/usr/bin/python

def fact(n):
	for I in range(1,n):
		n = n * I
	return n

print "Factorielle : {}".format(fact(3))
assert fact(3) == 6, fact(3)
