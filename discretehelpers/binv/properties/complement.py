from functools import cached_property


@cached_property
def complement(self):

    from discretehelpers.binv import Binv

    result = Binv([not val for val in self.vector])
    
    return result
