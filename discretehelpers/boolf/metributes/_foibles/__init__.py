from functools import cached_property


@cached_property
def is_odd(self):
    return self.root[0]


@cached_property
def is_odious(self):
    return self.root[-1]


@cached_property
def is_ugly(self):
    return self.is_odd ^ self.is_odious


@cached_property
def is_male(self):
    return bool(self.root.weight % 2)
