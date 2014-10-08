class A(object):
    def __init__(self):
        self.value = 10
        self.name = 'toto'
    def __str__(self):
        return 'object of class A({}, {})'.format(self.name, self.value)
    def __repr__(self):
        return 'repr of A'

a = A()
print str(a)
print a
print repr(a)
