def fact(n):
	if n > 0:
		return fact(n-1) * n
	else:
		return 1

print "Factorielle : {} ".format(fact(5))
