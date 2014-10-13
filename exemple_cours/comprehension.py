l = ['toto', 'tata', 'tutu']

l2 = []
for i in l:
    if 'o' in i:
        l2.append(i)

print l2

l3 = [(i, len(i)) for i in l]

print "l3", l3
