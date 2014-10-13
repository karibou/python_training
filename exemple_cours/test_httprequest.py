import unittest

from httprequest import create_url


class HttpRequestTC(unittest.TestCase):

    def test_create_url(self):
        d = {'a': 12, 'b': 13}
        base_url = 'http://toto.com'
        res = create_url(base_url, d)
        expected1 = 'http://toto.com?a=12&b=13'
        expected2 = 'http://toto.com?b=13&a=12'
        self.assertIn(res, [expected1, expected2])



if __name__ == '__main__':
    unittest.main()
