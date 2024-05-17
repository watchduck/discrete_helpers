from functools import cached_property

from copy import deepcopy


@cached_property
def blight(self):

    result = deepcopy(self.bloat)

    for atomkey in self.onesided_atomkeys:
        split = self.splits[atomkey]
        if split[0] == set():  # the set is empty, so its complement is the universe
            result.set_comp(atomkey, -1)
        else:  # the set is the universe
            result.set_equal(atomkey, -1)

    return result
