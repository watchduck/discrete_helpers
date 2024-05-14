import operator


def _bitwise(self, name, other):
    from .. import Binv

    length = len(self)
    if name in ['and', 'or', 'xor']:
        op = {
            'and': operator.and_,
            'or': operator.or_,
            'xor': operator.xor
        }[name]
        vector = [op(self[i], other[i]) for i in range(length)]
        return Binv(vector)
    elif name == 'smaller':
        if self == other:
            return False
        for i in range(length):
            if self[i] > other[i]:
                return False
        return True


def __and__(self, other):
    return _bitwise(self, 'and', other)


def __or__(self, other):
    return _bitwise(self, 'or', other)


def __xor__(self, other):
    return _bitwise(self, 'xor', other)


def bitwise_smaller(self, other):
    return _bitwise(self, 'smaller', other)


def __invert__(self):
    return self.complement
