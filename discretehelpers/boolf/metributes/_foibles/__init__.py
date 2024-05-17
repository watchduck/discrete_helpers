from functools import cached_property


@cached_property
def is_odd(self):
    return self.dense_tt[0]


@cached_property
def is_odious(self):
    return self.dense_tt[-1]


@cached_property
def is_ugly(self):
    return self.is_odd ^ self.is_odious


@cached_property
def dense_is_sharp(self):
    return bool(self.dense_tt.weight % 2)
