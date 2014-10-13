d = {'toto':3}
import traceback
d = {}

def mysleep():
    i = 10000
    while i > 0:
        i -= 1

try:
    var = d['toto']
except KeyError as err:
    print 'oups error ', err.args
    var = 3
else:
    print 'tout est ok'

print 'var', var
