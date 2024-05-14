from functools import cached_property

from discretehelpers.a import true_except

from discretehelpers.set_part import SetPart

from discretehelpers.boolf.ex import BoolfNotBlightlessError


@cached_property
def bundle_grid_partitions(self):

    true_except(self.is_blightless, BoolfNotBlightlessError)

    bundles = [tuple(bundle) for bundle in self.bundles]  # tuples instead of lists

    result = dict()
    for bundle in bundles:
        pairs = self.bundle_overlap_counts[bundle][3]  # only those with count 3 are relevant here
        partition = SetPart()
        for a, b in pairs:
            partition.merge_pair(a, b)
        result[bundle] = partition

    return result
