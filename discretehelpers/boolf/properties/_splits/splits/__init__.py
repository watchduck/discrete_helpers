from functools import cached_property

from discretehelpers.boolf.a import spotints_to_splits


@cached_property
def splits(self):

    return spotints_to_splits(self.fullspots, self.valency)
