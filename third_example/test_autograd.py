import unittest

from hypothesis import given

from hypothesis.strategies import floats, integers, sampled_from
from hypothesis.extra.numpy import arrays

import autograd.numpy as np
from autograd import elementwise_grad as egrad

class TestAutoGrad(unittest.TestCase):

    @given(arr=arrays(np.float, integers(min_value=1), elements=floats(allow_nan=False, allow_infinity=False)))
    def test_simple(self, arr):

        shouldbe_cos = egrad(np.sin)

        self.assertTrue(np.isclose(shouldbe_cos(arr), np.cos(arr)).all())

    if __name__ == '__main__':
        unittest.main()
