#!/usr/bin/python

def prime(N):
	if not isinstance(N,int):
		print "Pas un entier"
		return

	crible = range(N+1)
	
	crible[0]=None
	crible[1]=None
	
	Index=0
	
	while Index < N:
		if crible[Index] == None:
			Index+=1
			continue
		for I in range(Index,N+1,Index):
			if I is not Index:
				crible[I]=None
		Index+=1
	return [i for i in crible if i is not None]
		
	
print prime(25)
