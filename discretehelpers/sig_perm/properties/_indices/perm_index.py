from functools import cached_property


@cached_property
def perm_index(self):

    result = self.perm.left_rank

    return result
