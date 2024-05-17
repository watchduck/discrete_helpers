from functools import cached_property


@cached_property
def split_pairs_with_3_overlaps(self):

    result = []
    for pair, count in self.splits_overlap_counts.items():
        if count == 3:
            result.append(pair)

    return result
