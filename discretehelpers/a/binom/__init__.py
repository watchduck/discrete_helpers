from math import factorial

"""
n over k is the number of k-subsets of an n-set.
"""


def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))
