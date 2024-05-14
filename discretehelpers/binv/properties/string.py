from functools import cached_property

from discretehelpers.binv.a import to_string


@cached_property
def string(self):

    result = to_string(self.vector)
    
    return result
