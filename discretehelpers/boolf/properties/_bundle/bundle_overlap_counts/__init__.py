from functools import cached_property

from discretehelpers.a import true_except

from discretehelpers.boolf.ex import BoolfNotBlightlessError


@cached_property
def bundle_overlap_counts(self):

    true_except(self == self.bloatless_boolf, BoolfNotBlightlessError)

    # prepare variables
    split_pairs = self.splits_overlap_counts.keys()  # just the pairs without the counts
    bundles = [tuple(bundle) for bundle in self.bundles]  # tuples instead of lists

    # preallocate result
    result = dict()
    for bundle in bundles:
        result[bundle] = {3: [], 4: []}

    # assign pairs to bundles, and within that to the respective count
    for a, b in split_pairs:
        for bundle in bundles:
            if a in bundle and b in bundle:  # if the pair belongs to that bundle
                count = self.splits_overlap_counts[(a, b)]
                result[bundle][count].append((a, b))

    return result
