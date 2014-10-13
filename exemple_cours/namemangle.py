class NameM(object):

    def __init__(self):
        self.__name = 'nameMangled'
        self._priv = 42
        self.x = 156

    def get_priv(self):
        return self._priv

    def printMoi(self):
        print '{}'.format(self.__name)
