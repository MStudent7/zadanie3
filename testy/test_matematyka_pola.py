import unittest
from biblioteka.matematyka_pola import pole_kwadratu, pole_prostokata, pole_trojkata

class TestMatematykaPola(unittest.TestCase):

    def test_pole_kwadratu(self):
        self.assertEqual(pole_kwadratu(4), 16)
        self.assertEqual(pole_kwadratu(0), 0)

    def test_pole_prostokata(self):
        self.assertEqual(pole_prostokata(2, 3), 6)
        self.assertEqual(pole_prostokata(0, 5), 0)

    def test_pole_trojkata(self):
        self.assertEqual(pole_trojkata(4, 5), 10.0)
        self.assertEqual(pole_trojkata(0, 5), 0.0)

if __name__ == "__main__":
    unittest.main()
