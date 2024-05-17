import numpy as np

from discretehelpers.binv.a import binary_length
from discretehelpers.a import have, true_except, try_except

from .ex import *


class Binv(object):

    def __init__(self, vector=None, intval=None, exposet=None, length=None, minimal_length=None):

        case_vector = have(vector) and not have(intval) and not have(exposet) and not have(length)

        case_intval = have(intval) and not have(vector) and not have(exposet)
        case_intval_only = case_intval and not (have(length) or have(minimal_length))
        case_intval_length = case_intval and (have(length) or have(minimal_length))

        case_exposet = have(exposet) and not have(vector) and not have(intval)
        case_exposet_only = case_exposet and not (have(length) or have(minimal_length))
        case_exposet_length = case_exposet and (have(length) or have(minimal_length))

        true_except(case_vector or case_intval or case_exposet, ArgumentError)

        trust = False

        if case_vector:

            true_except(type(vector) in [list, np.ndarray, tuple, str, Binv], VectorTypeError)

            if len(vector) == 0:
                self.set_empty()
                return

            if type(vector) == str:
                vector = vector.replace(' ', '')
            elif type(vector) == Binv:
                trust = True
                vector = vector.vector

            if not trust:
                for e in vector:
                    try_except(lambda: int(e), do_raise=VectorEntryError, if_raised=ValueError)
                    true_except(int(e) in [0, 1], VectorEntryError)

        elif case_intval:

            true_except(type(intval) == int and intval >= 0, IntvalError)
            if case_intval_only:
                if intval == 0:
                    self.set_empty()
                    return
                vector = "{0:b}".format(intval)[::-1]
            elif case_intval_length:
                if have(length):
                    true_except(length >= binary_length(intval), LengthError)
                else:
                    length = max(minimal_length, binary_length(intval))
                vector = "{0:b}".format(intval).zfill(length)[::-1]

        elif case_exposet:

            true_except(type(exposet) in [set, list, tuple], IndicesTypeError)
            for e in exposet:
                true_except(type(e) == int, IndicesEntryError)
            if case_exposet_only:
                if len(exposet) == 0:
                    self.set_empty()
                    return
                else:
                    length = max(exposet) + 1
            elif case_exposet_length:
                if have(length):
                    if len(exposet) > 0:
                        true_except(length > max(exposet), LengthError)
                else:
                    length = max(minimal_length, max(exposet) + 1)
            vector = [False] * length
            for i in exposet:
                vector[i] = True

        self.vector = vector if trust else [bool(int(e)) for e in vector]
        self.set_dummies()
        self.required_length = max(self.exposet) + 1 if self.exposet else 0

    def set_empty(self):
        self.vector = []
        self.set_dummies()
        self.required_length = 0

    def set_dummies(self):
        metribute_names = [
            'string', 'pretty', 'complement', 'length', 'weight', 'changes', 'intval', 'exposet', 'set_part'
        ]
        for name in metribute_names:
            setattr(self, '_' + name, None)

    def flip_bit(self, position):
        assert position < self.length
        vector = self.vector.copy()
        vector[position] = not vector[position]
        return Binv(vector)

    from .metributes import string, pretty, complement, length, weight, changes, intval, exposet, set_part, reverse

    def has_index(self, key):  # basically like `__getitem__(key)`, but works also for keys beyond the length
        return key in self.exposet

    def __getitem__(self, key):  # This also makes `sum()` work. Compare `has_index`.
        return self.vector[key]

    def __add__(self, other):
        assert isinstance(other, Binv)
        return Binv(self.vector + other.vector)

    def __eq__(self, other):
        assert isinstance(other, Binv)
        return self.vector == other.vector

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.vector)

    from .methods.bitwise import __and__, __or__, __xor__, bitwise_smaller, __invert__
    from .methods.str import __str__, __hash__
    from .methods.comparisons import __lt__, __gt__, __le__, __ge__
