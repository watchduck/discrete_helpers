from functools import cached_property

import factoradic

from discretehelpers.a import have, true_except
from discretehelpers.perm.a import right_inversion_count

from .ex import PermNotFiniteError


@cached_property
def right_rank(self):
    """lexicographic rank based on right inversion count"""

    true_except(not have(self.perilen), PermNotFiniteError)

    if self.neutral:
        result = 0

    ric = right_inversion_count(self.sequence())
    ric_reflected = ric[::-1]
    return factoradic.from_factoradic(ric_reflected)
