from functools import cached_property


@cached_property
def intval(self):

    result = 0
    for a, b in self.pairs:
        exponent = ((b**2 - b) // 2) + a
        result += 2 ** exponent

    return result
