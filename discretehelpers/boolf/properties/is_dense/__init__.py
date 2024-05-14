from functools import cached_property


@cached_property
def is_dense(self):

    return self.adicity == self.valency
