from functools import cached_property


@cached_property
def weight(self):
    
    result = sum(self.vector)
    
    return result
