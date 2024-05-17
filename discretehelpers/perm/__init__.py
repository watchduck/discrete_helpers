import numpy as np

from discretehelpers.a import true_except, is_natural, have, slice_to_range
from .a import broaden_moved, reduce_period

from .ex import *


class Perm(object):
    
    def __init__(self, arg=None, perilen=None):
        """
        `arg` can have three different formats:
        - list of integers: second line of two-line notation
        - list of lists of integers: cycles
        - dict with integers as keys and values (fixed points not required)
        `perilen` is the period length. The pattern of this length repeats indefinitely.
        """

        if not have(arg) or arg == list():
            self.set_neutral()
            return

        true_except(type(arg) in [list, tuple, dict], ArgTypeError)

        mapping = dict()
        if arg and type(arg) in [list, tuple]:  # if non-empty list or tuple
            element_type = type(arg[0])
            if element_type == int:  # `arg` is sequence, i.e. lower line of two-line notation
                true_except(sorted(arg) == list(range(len(arg))), SequenceError)
                for key, val in enumerate(arg):
                    if key != val:
                        mapping[key] = val
            elif element_type == list:  # `arg` is list of cycles
                for cycle in arg:
                    true_except(type(cycle) == list and all(is_natural(e) for e in cycle), CyclesError)
                    length = len(cycle)
                    for key, val in enumerate(cycle):
                        map_from = val
                        map_to = cycle[(key + 1) % length]
                        if map_from != map_to:
                            mapping[map_from] = map_to
        elif type(arg) == dict:
            true_except(sorted(arg.keys()) == sorted(arg.values()), DictError)
            for key, val in arg.items():
                if key != val:
                    mapping[key] = val

        if mapping == dict():
            self.set_neutral()
            return

        if have(perilen):
            moved = set(mapping.keys())
            true_except(is_natural(perilen), PeriodLengthNotNaturalError)
            true_except(perilen >= 2, PerilenTooSmallError)
            true_except(perilen > max(moved), PerilenTooSmallError)
            mapping, perilen = reduce_period(mapping, perilen)

        self.neutral = False
        self.mapping = mapping
        self.moved = set(self.mapping.keys())
        self.perilen = perilen
        if have(perilen):
            self.length = perilen
        else:
            self.length = max(self.moved) + 1 if not self.neutral else 0

    def set_neutral(self):
        self.neutral = True
        self.mapping = dict()
        self.moved = set()
        self.perilen = None
        self.length = 0

    from .metributes import inverse, cycles, order, left_rank, right_rank, cycle_partition, \
        inversion_set, parity, schoute_perm

    def __getitem__(self, arg):
        if is_natural(arg):
            if self.neutral:
                return arg
            if self.perilen is None:
                if arg in self.moved:
                    return self.mapping[arg]
                else:
                    return arg
            else:
                remainder = arg % self.perilen
                if remainder in self.moved:
                    return self.mapping[remainder] + arg - remainder
                else:
                    return arg
        elif isinstance(arg, slice):
            return [self[i] for i in slice_to_range(arg, self.length)]

    def __eq__(self, other):
        true_except(isinstance(other, Perm), OtherNotPermError)
        if self.neutral and other.neutral:
            return True
        else:
            return self.mapping == other.mapping and self.perilen == other.perilen

    def __str__(self):
        if self.neutral:
            return 'Perm()'
        cycles = str(list(self.cycles))
        if have(self.perilen):
            return f'Perm({cycles}, perilen={self.perilen})'
        else:
            return f'Perm({cycles})'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __mul__(self, other):  # a * b means a after b (function composition)
        true_except(isinstance(other, Perm), OtherNotPermError)

        if self.neutral:
            return other
        if other.neutral:
            return self

        perilen_used = is_natural(self.perilen) and is_natural(other.perilen)
        perilen_none = self.perilen is None and other.perilen is None
        true_except(perilen_used or perilen_none, OtherPerilenMismatchError)

        if perilen_none:
            moved = self.moved.union(other.moved)
            perilen = None

        if perilen_used:
            perilen, moved = broaden_moved(self.perilen, other.perilen, self.moved, other.moved)

        mapping = dict()
        for i in moved:
            mapping[i] = self[other[i]]
        return Perm(mapping, perilen)

    def __pow__(self, exponent):

        if exponent == 0:
            return Perm()
        if exponent == 1:
            return self
        if exponent == -1:
            return self.inverse

        if exponent > 1:
            result = self
            for i in range(exponent - 1):
                result *= self
            return result
        elif exponent < -1:
            inverse = self.inverse
            result = inverse
            for i in range(-exponent - 1):
                result *= inverse
            return result

    def sequence(self, length=None):
        if have(length):
            if have(self.perilen):
                true_except(length % self.perilen == 0, LengthMismatchPerilenError)
            else:
                true_except(length >= self.length, LengthTooSmallError)
        else:
            length = self.perilen if have(self.perilen) else self.length
        return [self[i] for i in range(length)]

    def apply_on_vector(self, vector):
        arg_type = type(vector)
        inv = self.inverse
        return arg_type([vector[inv[i]] for i in range(len(vector))])

    def cycles_dynamic(self, length=None):
        true_except(have(self.perilen), NotPeriodicError)
        if have(length):
            true_except(length % self.perilen == 0, LengthMismatchPerilenError)
        else:
            length = self.perilen
        times = length // self.perilen
        result = []
        for i in range(times):
            for cycle in self.cycles:
                increased_cycle = np.array(cycle) + i * self.perilen
                result.append(list(increased_cycle))
        return result
