from functools import cached_property


@cached_property
def bloatless_boolf(self):

    from discretehelpers.binv import Binv
    from discretehelpers.boolf import Boolf

    if self.is_constant:
        return self
    if self.bloat_boolf == self:
        return Boolf('1')
    else:
        major_binv = self.dense_tt
        major_fullspots = major_binv.exposet
        minor_fullspots = set(self.bloatless_spotint(_) for _ in major_fullspots)
        minor_binv = Binv(exposet=minor_fullspots, length=2 ** self.number_of_distinct_splits)
        minor_atomvals = [self.atomvals[_] for _ in self.bloatless_atomkeys_undeflated]
        return Boolf(minor_binv, minor_atomvals)
