from functools import cached_property


@cached_property
def is_root(self):

    return self.adicity == self.valency
