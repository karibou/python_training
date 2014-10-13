import unittest

from rocket import Vect


class VectTC(unittest.TestCase):

    def test__add__(self):
        v1 = Vect(1, 2)
        v2 = Vect(3, 4)
        v3 = v1.__add__(v2)
        self.assertEqual(v3.x, 4)
        self.assertEqual(v3.y, 6)

    def test_add(self):
        v1 = Vect(1, 2)
        v2 = Vect(3, 4)
        self.assertEqual(v1 + v2, Vect(4,6))

    def test_eq(self):
        v1 = Vect(1,1)
        v2 = Vect(1,1)
        self.assertEqual(v1, v2)

    def test_repr(self):
        v1 = Vect(1,2)
        self.assertEqual(repr(v1), '(1, 2)')

    def test_mul(self):
        v1 = Vect(4, 2)
        self.assertEqual(v1 * 10, Vect(40, 20))
        self.assertEqual(10 * v1, Vect(40, 20))


