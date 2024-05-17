from functools import cached_property

from discretehelpers.set_part_comp import SetPartComp


@cached_property
def bloat(self):

    result = SetPartComp()

    for (a, b), splits_are_equal in self.splits_equal.items():
        if splits_are_equal:
            if self.splits[a] == self.splits[b]:  # sets are equal
                result.set_equal(a, b)
            else:  # sets are complements
                result.set_comp(a, b)

    return result
