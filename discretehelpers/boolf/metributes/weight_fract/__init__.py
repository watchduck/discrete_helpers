from functools import cached_property

from fractions import Fraction


@cached_property
def weight_fract(self):

    num = sum(self.root)
    den = len(self.root)
    return Fraction(num, den)
