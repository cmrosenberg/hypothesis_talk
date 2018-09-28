import itertools
import sys

# Example adopted from Hillel Wayne's talk "Beyond Unit Tests"
# https://hillelwayne.com/talks/beyond-unit-tests/

def smart(list_of_ints):

    if len(list_of_ints) < 2:
        raise ValueError("only works for lists of at least two elements")

    list_of_ints.sort()

    return list_of_ints[-1] * list_of_ints[-2]

def slow(list_of_ints):

    if len(list_of_ints) < 2:
        raise ValueError("only works for lists of at least two elements")

    maxprod = -sys.maxsize

    for a,b in itertools.combinations(list_of_ints, 2):
        maxprod = max(a * b, maxprod)

    return maxprod
