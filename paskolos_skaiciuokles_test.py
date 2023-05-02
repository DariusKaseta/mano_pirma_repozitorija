import unittest
from paskolos_skaiciuokle import PaskolosSkaiciuokle
from decimal import Decimal


class TestPaskolosSkaiciuokle(unittest.TestCase):
    def test_menesine_imoka(self):
        skaiciuokle = PaskolosSkaiciuokle()
        self.assertAlmostEqual(skaiciuokle.menesine_imoka(10000, 0.1, 5), 212.47, 2)
        self.assertAlmostEqual(skaiciuokle.menesine_imoka(5000, 0.05, 10), 53.09, delta=0.1)
        # self.assertAlmostEqual(skaiciuokle.menesine_imoka(15000, 0.07, 8), 212.44, 2)
        
    def test_bendra_suma(self):
        skaiciuokle = PaskolosSkaiciuokle()
        self.assertAlmostEqual(skaiciuokle.bendra_suma(10000, 0.1, 5), Decimal('12748.23'), 2)
        self.assertAlmostEqual(skaiciuokle.bendra_suma(5000, 0.05, 10), Decimal('6365.24'), 2)
        self.assertAlmostEqual(skaiciuokle.bendra_suma(15000, 0.07, 8), Decimal('20333.17'), 2)

if __name__ == '__main__':
    unittest.main()