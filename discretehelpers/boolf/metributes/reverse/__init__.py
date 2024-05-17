from functools import cached_property


@cached_property
def reverse(self):

    from discretehelpers.boolf import Boolf

    return Boolf(
        self.dense_tt[::-1],
        atomvals=self.atomvals
    )
