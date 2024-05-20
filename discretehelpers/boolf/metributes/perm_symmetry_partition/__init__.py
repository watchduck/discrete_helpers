from functools import cached_property

from discretehelpers.sig_perm import SigPerm
from discretehelpers.set_part import SetPart


@cached_property
def perm_symmetry_partition(self):

    boolf = self.root_boolf
    tt = boolf.tt(self.adicity)

    domain = list(range(2 ** self.adicity))

    setpart = SetPart([], domain=domain)

    faction = boolf.ec_faction()
    block = faction.get_block_from_label(boolf)

    for perm_index in block:
        sig_perm = SigPerm(pair=(0, perm_index))
        for pre_place in domain:
            post_place = sig_perm.apply_on_natural_number(pre_place)
            if tt[post_place] == tt[pre_place]:
                setpart.merge_pair(pre_place, post_place)

    return setpart
