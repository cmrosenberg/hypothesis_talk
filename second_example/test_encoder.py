import unittest

from hypothesis import assume, given
from hypothesis.strategies import text

from sklearn.feature_extraction.text import CountVectorizer

class TestEventEncoder(unittest.TestCase):

    @given(text())
    def test_featureextraction(self, s):
        assume(s != "")

        distinct_chars = len(set(s))

        cv_instance = CountVectorizer(analyzer='char')

        cv_instance.fit_transform([s])

        print("distinct chars is", distinct_chars, " while features are ", len(cv_instance.get_feature_names()))

        self.assertEqual(len(cv_instance.get_feature_names()), distinct_chars)

if __name__ == '__main__':
    unittest.main()
