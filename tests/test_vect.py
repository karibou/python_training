import math
import unittest
import rocket

class VectTest(unittest.TestCase):
    def setUp(self):
        self.v = rocket.Vect(2,2)

    def test_init(self):
        print "x:{}, y:{}".format(self.v.x, self.v.y)
        self.assertEqual(self.v.x,2.0)
        self.assertEqual(self.v.y,2.0)

    def test_add(self):
        b = rocket.Vect(1,1)
#        res = b.__add__(self.v)      __add__ is recognized as + by python
        res = self.v + b
        self.assertEqual(res.x, 3.0)
        self.assertEqual(res.y, 3.0)

    def test_mul(self):
        res = self.v * 3
        self.assertEqual(res.x, 6.0)
        self.assertEqual(res.y, 6.0)
        
    def test_rmul(self):
        res = 3 * self.v
        self.assertEqual(res.x, 6.0)
        self.assertEqual(res.y, 6.0)
        
    def test_div(self):
        res = self.v / 2
        self.assertEqual(res.x, 1.0)
        self.assertEqual(res.y, 1.0)
        
    def test_div(self):
        res = 2 / self.v
        self.assertEqual(res.x, 1.0)
        self.assertEqual(res.y, 1.0)
        
    def test_sub(self):
        b = rocket.Vect(1,1)
        res = self.v - b
        self.assertEqual(res.x, 1.0)
        self.assertEqual(res.y, 1.0)
        
    def test_abs(self):
        res  = self.v.abs()
        self.assertEqual(self.v.abs(),math.sqrt(2 ** 2 + 2 ** 2))
# 
#     def abs(self):
#         return math.sqrt(self.x**2 + self.y**2)
