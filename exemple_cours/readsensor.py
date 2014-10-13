f = open('/home/formateur/start/io/input/sensor.txt')
l = f.readline()
headers = l.split()


print 'headers', headers
d = {}
for h in headers:
    d[h] = []

for line in f:
    fields = line.split()
    if not fields:
        continue
    for index, field in enumerate(fields):
        header = headers[index]
        d[header].append( field)



f.close()
print 'resultat : '
print d

f2 = open('mod_mesures.py', 'w')
f2.write('unevariable == {}'.format(d))

f2.close()

# {'Vcc': [12.1, 12.1], 'Vpp': [5.02, 5.03]}
