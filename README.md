
# Property-based testing and the Hypothesis framework

This repository holds the example code and some notes for a talk I gave at the
Simula bi-weekly tools-meetup on Property-based testing and the [Hypothesis testing framework](https://hypothesis.works/) on Friday September 28th, 2018.

## What is Property-based testing?

As the author of Hypothesis [points out in an article on this very question](https://hypothesis.works/articles/what-is-property-based-testing/),
it is hard to give a crisp definition that captures everything associated with the term "property-based testing".
The gist of it is to try to test that certain properties of your program holds by automatically (and often randomly) generating example instances where the property should hold. It frees you from the tedium of coming up with (counter)examples in the form of unit tests, and helps you find adversarial examples that break your code.

I recommend reading [the aforementioned article](https://hypothesis.works/articles/what-is-property-based-testing/) if you want to explore the term "property-based  testing" more.

## What is Hypothesis?

[Hypothesis](https\://hypothesis.works/) is a property-based tesing framework mainly targeting Python but also [other platforms](https://github.com/HypothesisWorks/hypothesis). It helps you write property-based tests by giving you lots of options for automatically generating example data of different kinds (even [numpy arrays and pandas dataframes](https://hypothesis.readthedocs.io/en/latest/numpy.html)!). It integrates nicely with your existing unit testing framework, making it easy to gradually adopt Property-based testing.

Hypothesis is being used by several [companies](https://hypothesis.readthedocs.io/en/latest/endorsements.html) and [open source projects](https://hypothesis.readthedocs.io/en/latest/usage.html). The payment service company Stripe uses it to extensively [test their machine learning model training pipeline](https://hypothesis.readthedocs.io/en/latest/endorsements.html), for example.

## Code examples

The talk revolved around a few code examples where I showcased different aspects of using Hypothesis.

The first example discussed an example borrowed from Hillel Wayne's [excellent talk](https://hillelwayne.com/talks/beyond-unit-tests/): A function that finds the maximal product of two elements from a list of integers. I show how quickly Hypothesis can find an example that breaks a "clever" implementation.

The second example discusses the challenge of checking whether [CountVectorizer from scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) behaves as expected when tokenizing on chars. In `test_encoder.py` I check whether CountVectorizer can handly any unicode input. In `test_restricted`, I check whether CountVectorizer can cope when explicitly asked not to lowercase its inputs and receiving a much more restricted set of unicode letters.

The third example shows a simple way of writing an extended unit test for the [autograd](https://github.com/HIPS/autograd) differentiation library: We use autograd to find the derivative of `np.sin`, and then check whether it behaves like `np.sin` for a bunch of input arrays.

### Installing the prereqs needed for the code examples

## Resources

While researching Hypothesis and Property-based testing I benefitted greatly
from the following:

- The official [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/)
- Alex Chan's [talk on Hypothesis and AFL](https://alexwlchan.net/talks/qcon2017/)
- Hillel Wayne's [talk on going beyind unit tests with property-based testing and contracts](https://hillelwayne.com/talks/beyond-unit-tests/)
- Scott W. Found's article on [Choosing properties for property-based testing](https://fsharpforfunandprofit.com/posts/property-based-testing-2/)
