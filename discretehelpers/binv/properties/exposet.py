from functools import cached_property


@cached_property
def exposet(self):

    result = set(key for key, val in enumerate(self.vector) if val)
    
    return result
