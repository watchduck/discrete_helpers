from functools import cached_property

import numpy as np


@cached_property
def order(self):
    """lowest positive exponent that will produce the identity"""

    if self.neutral:
        self.order = 1
        return 1

    cycle_lengths = [len(cycle) for cycle in self.cycles]
    result = np.lcm.reduce(cycle_lengths)

    return result
