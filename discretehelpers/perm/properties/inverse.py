from functools import cached_property


@cached_property
def inverse(self):

    from discretehelpers.perm import Perm

    inverse_map = dict((self.mapping[key], key) for key in self.mapping.keys())
    result = Perm(inverse_map, self.perilen)

    return result
