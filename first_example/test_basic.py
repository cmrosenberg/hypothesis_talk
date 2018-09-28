import unittest
import maxprod

class TestMaxProd(unittest.TestCase):


    def test_basic(self):

        example = [1, 5, 7, 3]

        self.assertEqual(maxprod.smart(example), 5 * 7)

if __name__ == '__main__':
    unittest.main()
