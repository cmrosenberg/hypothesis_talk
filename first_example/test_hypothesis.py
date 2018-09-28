import unittest
import maxprod

from hypothesis import given
from hypothesis import strategies as st

class TestMaxProdWithHypothesis(unittest.TestCase):

    @given(st.lists(elements=st.integers(), min_size=2))
    def test_agrees(self, xs):
        self.assertEqual(maxprod.smart(xs), maxprod.slow(xs))

if __name__ == '__main__':
    unittest.main()
