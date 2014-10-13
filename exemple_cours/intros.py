class CacheMixin(object):
    def get_cached(self, member, compute_func):
        """retourne la valeur mise en cache ou la calcule"""
        if not hasattr(self, member):
            setattr(self, member, compute_func())
        return getattr(self, member)

    def flush_cache(self, member):
        """supprime la valeur mise en cache pour member"""
        if hasattr(self, member):
            delattr(self, member)

class A(CacheMixin):
    def computeMember(self):
        print 'computing...'
        return 2 ** 20
    def getExpensiveMember(self):
        return self.get_cached('cachedattr', self.computeMember)
a = A()
print a.getExpensiveMember()
print a.cachedattr
for attr in  dir(a):
    print attr, getattr(a, attr)


