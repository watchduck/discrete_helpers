from functools import cached_property

"""
`self.blot` uses atomkeys instead of atomvals. But the latter are used here.
"""


@cached_property
def blot_boolf(self):

    from discretehelpers.boolf import Boolf

    result = Boolf(True)

    for atomkey in self.onesided_atomkeys:
        is_universe = self.onesided_is_universe[atomkey]  # dict
        tt = '01' if is_universe else '10'  # nothing outside or nothing inside
        atomval = self.atomvals[atomkey]
        result &= Boolf(tt, [atomval])

    return result
