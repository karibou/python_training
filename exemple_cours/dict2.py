d = {'a':1, 'b':2, 'c':3}

d2 = {}

for k,v in d.items():
    #v = d[k]
    d2[v] = k

d2 = {v:k for k,v in d.iteritems()}

assert d2 == {1:'a', 2: 'b',3: 'c'}, 'pas bon %s' % d2
