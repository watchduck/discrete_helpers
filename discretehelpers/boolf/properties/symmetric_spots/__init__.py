from functools import cached_property

from discretehelpers.sig_perm import SigPerm
from discretehelpers.set_part import SetPart


@cached_property
def symmetric_spots(self):

    boolf = self.dense_boolf

    spots = boolf.fullspots  # same as `self.fullspots`

    result = SetPart([], domain=spots)

    clan = boolf.ec_clan()
    block = clan.get_block_from_label(boolf)

    for pair in block:
        sig_perm = SigPerm(pair=pair)
        for spot in spots:
            symmetric_spot = sig_perm.apply_on_natural_number(spot)
            result.merge_pair(spot, symmetric_spot)

    return result
