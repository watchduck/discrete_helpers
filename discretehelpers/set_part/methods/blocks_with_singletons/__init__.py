from discretehelpers.a import have

from discretehelpers.a import true_except

from .ex import *


def blocks_with_singletons(self, length=None, range_pair=None, elements=None):

    if not have(length) and not have(range_pair) and not have(elements):  # no arguments

        if self.domain == 'N':
            elements = range(self.length)
        elif self.domain == 'Z':
            low = min(self.non_singletons)
            high = max(self.non_singletons) + 1
            elements = range(low, high)
        else:
            elements = self.domain

    elif have(length) and not have(range_pair) and not have(elements):  # length (for domain N)

        true_except(self.domain == 'N', LengthNotAllowedError)
        true_except(type(length) == int, LengthWrongTypeError)
        true_except(length >= self.length, LengthMismatchError)
        elements = range(length)

    elif not have(length) and have(range_pair) and not have(elements):  # range pair (for domain Z)

        true_except(self.domain == 'Z', RangeNotAllowedError)
        low, high = range_pair
        true_except(type(low) == type(high) == int, RangeWrongTypeError)
        true_except(low <= min(self.non_singletons) and high > max(self.non_singletons), RangeMismatchError)
        elements = range(low, high)

    elif not have(length) and not have(range_pair) and have(elements):  # elements (not restricted by domain)

        true_except(type(elements) in [set, list, range], ElementsWrongTypeError)
        true_except(self.non_singletons.issubset(set(elements)), ElementsMismatchError)

    else:

        raise TooManyArgumentsError

    singletons = set(elements).difference(self.non_singletons)
    singleton_blocks = [[_] for _ in singletons]
    return sorted(self.blocks + singleton_blocks)
