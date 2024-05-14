from functools import cached_property

from itertools import combinations

from discretehelpers.boolf.a import count_split_regions


@cached_property
def splits_overlap_counts(self):

    result = dict()
    for index1, index2 in combinations(range(self.valency), 2):  # all 2-subsets of atom exposet
        result[(index1, index2)] = count_split_regions(self.splits[index1], self.splits[index2])

    return result
