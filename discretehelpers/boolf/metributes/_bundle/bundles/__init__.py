from functools import cached_property

from discretehelpers.a import have, true_except

from discretehelpers.set_part import SetPart

from discretehelpers.boolf.ex import BoolfNotBlightlessError


@cached_property
def bundles(self):

    true_except(self == self.bloatless_boolf, BoolfNotBlightlessError)

    bundle_part = SetPart()
    for pair, count in self.splits_overlap_counts.items():
        if count == 4:
            bundle_part.merge_pair(*pair)

    return bundle_part.blocks_with_singletons(self.valency)
