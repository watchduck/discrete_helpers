from functools import cached_property


@cached_property
def inversion_set(self):

    from itertools import combinations

    pairs = combinations(range(self.length), 2)
    result = set()
    for a, b in pairs:
        if self[a] > self[b]:
            result.add((a, b))

    return result
