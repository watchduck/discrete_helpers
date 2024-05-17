from functools import cached_property


@cached_property
def set_part(self):

    from discretehelpers.set_part import SetPart

    true_block = self.exposet
    universe = set(range(self.length))
    false_block = universe.difference(true_block)
    result = SetPart([true_block, false_block])

    return result
