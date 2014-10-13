"""simple 2D geometries"""

import math

class Point(object):
    """2D point"""
    def __init__(self, x, y):
        """x: abscissa, y: ordinate

        both are floating point numbers
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return str( (self.x, self.y) )

    def distance(self, point2):
        """euclidean distance with another point"""
        dx = self.x - point2.x
        dy = self.y - point2.y
        return math.sqrt(dx * dx + dy * dy)


class Figure(object):
    """generic form, abstract base class for all others"""
    type = None

    def __init__(self, points):
        self.points = points

    def __str__(self):
        return self.type + ' ' + str(self.points)

    def get_position(self):
        """return the first point of the figure"""
        return self.points[0]

    def perimeter(self):
        """return the figure's perimeter"""
        raise NotImplementedError(self)


class Circle(Figure):
    """a circle, defined by a center and a radius"""
    type = 'circle'

    def __init__(self, center, radius):
        """center is a point, radius a floating point number"""
        super(Circle, self).__init__([center])
        self.center = center
        self.radius = radius

    def __str__(self):
        return 'circle with radius ' + str(self.radius) + ' and center ' + str(self.center)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Polygone(Figure):
    """a polygone"""
    type = 'polygone'

    def perimeter(self):
        # create a list of consecutive points using a shift list of points to
        # zip
        shifted_points = self.points[1:]
        shifted_points.append(self.points[0])
        result = 0.
        for s1, s2 in zip(self.points, shifted_points):
            result += s1.distance(s2)
        return result


class Triangle(Polygone):
    """a triangle, defined by 3 points"""
    type = 'triangle'

    def __init__(self, sommet1, sommet2, sommet3):
        Polygone.__init__(self, [sommet1, sommet2, sommet3])


class Square(Polygone):
    """a quare, defined by a corner and a size"""
    type = 'square'

    def __init__(self, upleft_corner, size):
        pt2 = Point(upleft_corner.x+size, upleft_corner.y)
        pt3 = Point(upleft_corner.x+size, upleft_corner.y+size)
        pt4 = Point(upleft_corner.x, upleft_corner.y+size)
        Polygone.__init__(self, [upleft_corner, pt2, pt3, pt4])


class Quadrilateral(Polygone):
    """a quadrilateral, defined by 4 points"""
    type = 'quadrilateral'

    def __init__(self, sommet1, sommet2, sommet3, sommet4):
        Polygone.__init__(self, [sommet1, sommet2, sommet3, sommet4])


if __name__ == '__main__':
    for f in [Circle(Point(0, 0), 1),
              Triangle(Point(0, 0), Point(1, 0), Point(0, 1)),
              Square(Point(0,0), 2),
              Quadrilateral(Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)),
              ]:
        print '-'*80
        print f
        print 'perimeter:', f.perimeter()
