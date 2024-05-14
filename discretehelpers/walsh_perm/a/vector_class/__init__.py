from discretehelpers.a import true_except, is_natural, have, slice_to_range

from .ex import *


class Vector(object):
    
    def __init__(self, arg=None):

        if arg is None:
            arg = dict()

        true_except(type(arg) in [list, dict], TypeError)
        if type(arg) == list:
            true_except(all([is_natural(x) for x in arg]), TypeError)
        else:  # type(arg) == dict
            true_except(all([is_natural(x) for x in arg.keys()]), TypeError)
            true_except(all([is_natural(x) for x in arg.values()]), TypeError)

        mapping = dict()
        loop_arg = enumerate(arg) if type(arg) == list else arg.items()
        for key, val in loop_arg:
            if 2**key != val:
                mapping[key] = val

        self.mapping = mapping
        self.keys = list(mapping.keys())
        self.length = max(self.keys) + 1 if not mapping == dict() else 0

    def __getitem__(self, arg):
        if is_natural(arg):
            if arg in self.keys:
                return self.mapping[arg]
            else:
                return 2**arg
        elif isinstance(arg, slice):
            return [self[i] for i in slice_to_range(arg, self.length)]

    def __eq__(self, other):
        return self.mapping == other.mapping

    def __str__(self):
        return str(self.extend_to_length(self.length))

    def extend_to_length(self, length):
        true_except(length >= self.length, ExtendedLengthTooSmallError)
        return tuple([self[key] for key in range(length)])
