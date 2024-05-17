from functools import cached_property


@cached_property
def reverse(self):

    from discretehelpers.binv import Binv

    return Binv(self[::-1])
