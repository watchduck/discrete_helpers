from functools import cached_property


@cached_property
def keyneg_index(self):

    result = 0
    for key, val in enumerate(self.sequence()):
        if val < 0:
            result += 2 ** key

    return result
