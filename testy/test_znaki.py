import unittest
from biblioteka.znaki import liczenie_wspolglosek, liczenie_samoglosek, wielkie_litery, male_litery

class TestZnaki(unittest.TestCase):

    def test_liczenie_wspolglosek(self):
        self.assertEqual(liczenie_wspolglosek("hello"), 3)
        self.assertEqual(liczenie_wspolglosek("AEIOU"), 0)
        self.assertEqual(liczenie_wspolglosek("bcd123"), 3)

    def test_liczenie_samoglosek(self):
        self.assertEqual(liczenie_samoglosek("hello"), 2)
        self.assertEqual(liczenie_samoglosek("bcdf"), 0)
        self.assertEqual(liczenie_samoglosek("AEIOUY"), 6)

    def test_wielkie_litery(self):
        self.assertEqual(wielkie_litery("abc"), "ABC")

    def test_male_litery(self):
        self.assertEqual(male_litery("ABC"), "abc")

if __name__ == "__main__":
    unittest.main()
