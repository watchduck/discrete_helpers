from functools import cached_property

from discretehelpers.binv.a import to_pretty_string


@cached_property
def pretty(self):
    
    result = to_pretty_string(self.vector)

    return result
