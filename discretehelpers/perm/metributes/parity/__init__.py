from functools import cached_property


@cached_property
def parity(self):

    result = len(self.inversion_set) % 2

    return result
