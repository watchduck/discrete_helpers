from functools import cached_property


@cached_property
def onesided_is_universe(self):

    result = dict()
    for atomkey in self.onesided_atomkeys:
        inside = self.splits[atomkey][0]
        result[atomkey] = len(inside) > 0

    return result
