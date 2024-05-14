from functools import cached_property


@cached_property
def pair(self):

    result = (self.valneg_index, self.perm_index)

    return result
