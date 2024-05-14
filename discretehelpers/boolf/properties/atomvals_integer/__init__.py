from functools import cached_property

from discretehelpers.binv import Binv


@cached_property
def atomvals_integer(self):

    return Binv(exposet=self.atomvals).intval
