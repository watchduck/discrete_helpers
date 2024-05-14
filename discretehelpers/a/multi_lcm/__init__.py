from math import gcd
from functools import reduce

"""
calculate the least common multiple of a list of given numbers in Python
https://stackoverflow.com/questions/37237954
"""


def multi_lcm(integers):
    return reduce(lambda a,b: a*b // gcd(a,b), integers)
