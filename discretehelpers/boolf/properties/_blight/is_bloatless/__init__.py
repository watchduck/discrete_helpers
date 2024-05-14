from functools import cached_property


@cached_property
def is_bloatless(self):

    from discretehelpers.set_part_comp import SetPartComp

    return self.bloat == SetPartComp()
