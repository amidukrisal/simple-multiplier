import unittest
from app.logic import multiply

class TestMultiply(unittest.TestCase):
    def test_basic_multiplication(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)

if __name__ == '__main__':
    unittest.main()
