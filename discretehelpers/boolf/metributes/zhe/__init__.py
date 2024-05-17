from functools import cached_property

from discretehelpers.a import vector_to_int

from discretehelpers.boolf.a import vector_to_twin_gen


@cached_property
def zhe(self):

    tt = self.tt()
    twin_tt_gen = vector_to_twin_gen(tt, self.adicity)
    return vector_to_int(twin_tt_gen)
