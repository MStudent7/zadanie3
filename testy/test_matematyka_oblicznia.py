import unittest
from biblioteka.matematyka_obliczenia import rownanie_kwadratowe, oblicz_silnie

class TestMatematykaObliczenia(unittest.TestCase):

    def test_rownanie_kwadratowe(self):
        self.assertEqual(rownanie_kwadratowe(1, -3, 2), (2.0, 1.0))
        self.assertEqual(rownanie_kwadratowe(1, 2, 1), (-1.0,))
        self.assertEqual(rownanie_kwadratowe(1, 0, 1), "Brak rozwiązań rzeczywistych")

    def test_oblicz_silnie(self):
        self.assertEqual(oblicz_silnie(5), 120)
        self.assertEqual(oblicz_silnie(0), 1)
        with self.assertRaises(ValueError):
            oblicz_silnie(-1)

if __name__ == "__main__":
    unittest.main()
