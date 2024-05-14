def _bitwise(self, name, other):
    from ... import Boolf

    atomvals = sorted(set(self.atomvals).union(set(other.atomvals)))
    self_vector = self.tt(atomvals)
    other_vector = other.tt(atomvals)
    length = len(self_vector)
    if name in ['and', 'or', 'xor']:
        vector = {
            'and': self_vector & other_vector,
            'or': self_vector | other_vector,
            'xor': self_vector ^ other_vector
        }[name]
        return Boolf(vector, atomvals)
    elif name == 'smaller':
        if self_vector == other_vector:
            return False
        for i in range(length):
            if self_vector[i] > other_vector[i]:
                return False
        return True


def __and__(self, other):
    return _bitwise(self, 'and', other)


def __or__(self, other):
    return _bitwise(self, 'or', other)


def __xor__(self, other):
    return _bitwise(self, 'xor', other)


def bitwise_lt(self, other):
    return _bitwise(self, 'smaller', other)


def bitwise_gt(self, other):
    return other.bitwise_le(self)


def bitwise_le(self, other):
    return self == other or self.bitwise_lt(other)


def bitwise_ge(self, other):
    return other.bitwise_le(self)


def __invert__(self):
    return self.complement
