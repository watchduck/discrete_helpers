from functools import cached_property


@cached_property
def moved(self):
    return set(self.mapping.keys())
