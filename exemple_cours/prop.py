class A(object):

    def __init__(self):
        self.__x = 0

    def getx(self):
        print 'On recupere x'
        return self.__x

    def setx(self, val):
        print 'On change x'
        self.__x = val

    x = property(getx, setx, fdel=None,
            doc='une simple variable')

