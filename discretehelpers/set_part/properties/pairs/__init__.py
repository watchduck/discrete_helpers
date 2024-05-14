from functools import cached_property

from itertools import combinations


@cached_property
def pairs(self):

    result = set()
    for block in self.blocks:
        for pair in combinations(block, 2):
            result.add(pair)

    return result
