import math

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = 0

    def distance(self, otherpoint):
        self.dist = math.sqrt((self.x-otherpoint.x)**2 + (self.y-otherpoint.y)**2)
        return self.dist

class Figure(object):

    def __init__(self, points):
        self.points = points

    def position(self):
        pass

    def perimetre(self):
        pass

class Cercle(Figure):
    def __init__(self, centre, r):
        super(Cercle, self).__init__(centre)
        self.r = r

    def perimetre(self):
        return 2*math.pi*self.r

    def position(self):
        return self.points

class Carre(Figure):
    def __init__(self, p, dist):
        super(Carre, self).__init__(p)
        self.distance = dist

    def position(self):
        return self.points

    def perimetre(self):
        return 4*self.distance

class Triangle(Figure):
    def __init__(self, p1):
        super(Triangle, self).__init__([p1, p2, p3])

    def position(self):
        return self.points

    def perimetre(self):
        return self.p1.distance(self.points[2]) + self.p1.distance(self.points[3]) + self.p2.distance(self.points[3])

if __name__ == '__main__':
    p1 = Point(1,1)
    p2 = Point(1,2)
    p3 = Point(2,3)

    assert p1.distance(p2) == 1, 'pas bon {}'.format(p1.distance(p2))
    c = Cercle(p1,5)
    assert c.perimetre() == 2*5*math.pi, 'cercle perimetre pas bon %d'.format(c.perimetre())
    assert c.position() == p1, 'cercle position pas bon'

    ca = Carre(p1,5)
    assert ca.perimetre() == 4*5, 'carre perimetre pas bon'
    assert ca.position() == p1, 'carre position pas bon'

    t = Triangle([p1, p2, p3])
#    assert t.position() == [p1, p2, p3], 'triangle position pas bon'
    assert t.perimetre() == (p1.distance(p2) + p1.distance(p3) + p2.distance(p3)), 'triangle perimetre pas bon'

#vim: et ts=4 sw=4
