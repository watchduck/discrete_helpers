from functools import cached_property

import factoradic

from discretehelpers.a import have, true_except
from discretehelpers.perm.a import left_inversion_count

from .ex import PermNotFiniteError


@cached_property
def left_rank(self):
    """reverse colexicographic rank based on left inversion count"""

    true_except(not have(self.perilen), PermNotFiniteError)

    if self.neutral:
        return 0

    lic = left_inversion_count(self.sequence())
    return factoradic.from_factoradic(lic)
