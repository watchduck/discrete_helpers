from discretehelpers.a import true_except

from .ex import WrongTypeError


def inflated_fullspots(self, atomvals):
    true_except(type(atomvals) in [set, list, tuple], WrongTypeError)

    tt = self.tt(atomvals)
    return tt.exposet
