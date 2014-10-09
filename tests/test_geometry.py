import math
import unittest
import geometry

class GeometryTC(unittest.TestCase):
    def setUp(self):
        self.p1 = geometry.Point(1, 1)
        self.p2 = geometry.Point(1, 2)
        self.p3 = geometry.Point(2, 3)
    
    def test_distance(self):
        self.assertEqual(self.p1.distance(self.p2),1)
    
    def test_cercle_perimetre(self):
        c = geometry.Cercle(self.p1, 5)
        self.assertEqual(c.perimetre(),2 * 5 * math.pi)
    
    def test_cercle_position(self):
        c = geometry.Cercle(self.p1, 5)
        self.assertEqual(c.position(),self.p1)
    
    def test_carre_perimetre(self):
        ca = geometry.Carre(self.p1, 5)
        self.assertEqual(ca.perimetre(),4 * 5)
    
    def test_carre_position(self):
        ca = geometry.Carre(self.p1, 5)
        self.assertEqual(ca.position(),self.p1)
    
    
    def test_triangle_position(self):
        t = geometry.Triangle(self.p1, self.p2, self.p3)
        self.assertEqual(t.position(),[self.p1, self.p2, self.p3])
    
    def test_triangle_perimetre(self):
        t = geometry.Triangle(self.p1, self.p2, self.p3)
        self.assertEqual(t.perimetre(),self.p1.distance(self.p2) + 
        self.p1.distance(self.p3) + self.p2.distance(self.p3))
    
if __name__ == '__main__':
    unittest.main()
#vim: et ts=4 sw=4
