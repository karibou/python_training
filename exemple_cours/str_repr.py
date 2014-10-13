
class A(object):
    def __init__(self):
        self.value = 12
        self.name = 'toto'
    def __str__(self):
        return 'object of class A ({}, {})'.format(self.name, self.value)
    def __repr__(self):
        return 'toto'

a = A()
print str(a)
print repr(a)

