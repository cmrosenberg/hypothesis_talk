import unittest

from hypothesis import assume, given
from hypothesis.strategies import text

from sklearn.feature_extraction.text import CountVectorizer

from itertools import count

class TestEventEncoderFixed(unittest.TestCase):

    #Works for range(1000), starts to break for range(20000)...
    @given(text(alphabet=(chr(i + 512 + (i % 2) * 100) for i in range(1000))))

    def test_featureextraction(self, s):
        assume(s != "")

        distinct_chars = len(set(s))

        #Note how we explicitly set lowercase=False
        cv_instance = CountVectorizer(analyzer='char', lowercase=False, decode_error='strict')

        cv_instance.fit_transform([s])

        print("distinct chars is", distinct_chars, " while features are ", len(cv_instance.get_feature_names()))
        self.assertEqual(len(cv_instance.get_feature_names()), distinct_chars)

if __name__ == '__main__':
    unittest.main()
