from functools import cached_property


@cached_property
def valneg_index(self):

    result = self.binv.intval

    return result
