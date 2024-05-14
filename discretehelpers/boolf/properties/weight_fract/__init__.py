from functools import cached_property

from fractions import Fraction


@cached_property
def weight_fract(self):

    num = sum(self.dense_tt)
    den = len(self.dense_tt)
    return Fraction(num, den)
