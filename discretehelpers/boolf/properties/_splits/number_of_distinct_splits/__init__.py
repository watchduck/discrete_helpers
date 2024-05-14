from functools import cached_property


@cached_property
def number_of_distinct_splits(self):

    return len(self.splits_equality_blocks)
