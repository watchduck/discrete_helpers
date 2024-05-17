from functools import cached_property


@cached_property
def quadrant(self):

    return int(self.dense_tt[0]) + int(self.dense_tt[-1]) * 2
