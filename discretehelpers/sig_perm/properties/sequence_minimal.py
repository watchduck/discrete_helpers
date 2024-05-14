from functools import cached_property

from discretehelpers.a import logic_negate_vector


@cached_property
def sequence_minimal(self):

    result = logic_negate_vector(
        self.perm.sequence(self.length),
        which=self.binv.exposet
    )

    return result
