from functools import cached_property


@cached_property
def quadrant(self):

    return int(self.root[0]) + int(self.root[-1]) * 2
