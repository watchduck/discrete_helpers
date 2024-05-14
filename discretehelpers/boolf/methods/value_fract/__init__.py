from fractions import Fraction


def value_fract(self):
    tt = self.tt().string
    num = int(tt, 2)  # interpret truth table as big endian binary
    den = (1 << (1 << self.adicity)) - 1   # 2 ** (2 ** self.adicity) - 1
    return Fraction(num, den)
