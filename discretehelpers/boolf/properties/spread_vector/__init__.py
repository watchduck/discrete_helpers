from functools import cached_property


@cached_property
def spread_vector(self):

    return [self.atomvals[i] - i for i in range(self.valency)]
