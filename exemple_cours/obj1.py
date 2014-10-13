
class Camion(object):

    def __init__(self, poids, name):
        self.poids = poids
        self.name = name

    def printMoi(self):
        print '{} ({})'.format(self.name, self.poids)

class CamionPeugeot(Camion):

    def __init__(self):
        pass

class Camionette(CamionPeugeot):

    def __init__(self, a, b, marque):
        #Camion.__init__(self, a, b)
        super(Camionette, self).__init__(a, b)
        #self.poids = poids
        #self.name = name
        self.marque = marque
    def printMoi(self):
        print '{} ({})/{}'.format(self.name, self.poids, self.marque)

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line(object):

    def __init__(self, p1, p2):
        "p1 and p2 are Point"
        self.start = p1
        self.end = p2

