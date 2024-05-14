from functools import cached_property

from discretehelpers.a import have


@cached_property
def bloatless_atomkeys_undeflated(self):

    result = []
    for i, block in enumerate(self.splits_equality_blocks):
        pref = self.splits_preferred_side[i]
        if have(pref):
            new_atom = self.bloat.get_repr(pref)
        else:
            new_atom = min(block)
        result.append(new_atom)

    self.bloatless_atomkeys_undeflated = result
    return result
