from functools import cached_property


@cached_property
def length(self):
    
    result = len(self.vector)

    return result
