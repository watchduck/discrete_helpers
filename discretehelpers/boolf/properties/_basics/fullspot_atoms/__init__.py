from functools import cached_property

from discretehelpers.binv import Binv


@cached_property
def fullspot_atoms(self):

    result = dict()
    
    for spot_int in self.fullspots:
        spot_atomkeys = sorted(Binv(intval=spot_int).exposet)
        result[spot_int] = spot_atomkeys

    return result
