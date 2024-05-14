from functools import cached_property


@cached_property
def dense_boolf(self):

    from discretehelpers.boolf import Boolf

    if self.is_dense:
        return self
    else:
        return Boolf(fullspots=self.fullspots, atomvals=list(range(self.valency)))
