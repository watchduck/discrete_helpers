from functools import cached_property


@cached_property
def cycle_partition(self):

    from discretehelpers.set_part import SetPart

    if self.neutral:
        return SetPart([])

    return SetPart(self.cycles)
