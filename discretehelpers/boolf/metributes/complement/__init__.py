from functools import cached_property


@cached_property
def complement(self):

    from discretehelpers.boolf import Boolf

    return Boolf([not val for val in self.root], self.atomvals)
