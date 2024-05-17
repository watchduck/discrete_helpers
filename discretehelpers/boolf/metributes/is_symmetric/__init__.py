from functools import cached_property


@cached_property
def is_symmetric(self):

    result = True
    for layer in self.layered_tt:
        if len(set(layer)) > 1:
            result = False
            break

    return result
