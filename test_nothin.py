import unittest

def divide(x , y):
    return x / y

class TestAssertMethods(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(3 + 2, 5)

    def test_assertTrue(self):
        self.assertTrue(3 < 5)

    def test_assertFalse(self):
        self.assertFalse(5 < 3)

    def test_assertIs(self):
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)

    def test_assertIsNone(self):
        self.assertIsNone(None)


    def test_integer_division(self):
        self.assertEquals(divide(10, 2), 5)
        self.assertNotEquals(divide(2, 5), 0.4)
        self.assertAlmostEquals(divide(10, 3), 0.3333333, 17)

if __name__ == '__main__':
    unittest.main()
