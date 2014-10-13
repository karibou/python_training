prenoms = ['arthur', 'babar', 'celeste']
ages = [5,25,27]

d = {}

for i, p in enumerate(prenoms):
    d[p] = ages[i]

for p, a in zip(prenoms, ages):
    d[p] = a



assert d == {'arthur':5, 'babar':25, 'celeste':27}
