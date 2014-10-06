#!/usr/bin/python

N=20

crible = range(N+1)

crible[0]=None
crible[1]=None

Index=0

while Index <= N:
	print "crible[{0}] : {1}".format(Index,crible[Index])
	if crible[Index] == None:
		Index+=1
		continue
	Index2=Index+1
	while Index2 <= N:
		if crible[Index2] is not None and crible[Index2] % crible[Index] == 0:
			crible[Index2]=None
		Index2+=1
	Index+=1
print crible
	

