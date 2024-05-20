from discretehelpers.a import have
from discretehelpers.boolf.a import flat_to_layered


# main metribute (tuple of tuples)
@property
def layered_tt(self):
    return self._layered_tt


@layered_tt.setter
def layered_tt(self, val):
    self._layered_tt = val


@layered_tt.getter
def layered_tt(self):
    if have(self._layered_tt):
        return self._layered_tt

    some_magic(self)
    return self.layered_tt


# derived metribute (tuple of integers)
@property
def layered_weight(self):
    return self._layered_weight


@layered_weight.setter
def layered_weight(self, val):
    self._layered_weight = val


@layered_weight.getter
def layered_weight(self):
    if have(self._layered_weight):
        return self._layered_weight

    some_magic(self)
    return self.layered_weight


def some_magic(self):
    """function to create 3 metributes"""
    vector = [int(_) for _ in self.root]
    self.layered_tt = flat_to_layered(vector)
    self.layered_weight = tuple([sum(_) for _ in self.layered_tt])
