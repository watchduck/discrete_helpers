from functools import cached_property


@cached_property
def complement_distance(self):

    if self.neutral:
        result = 0
    else:
        sequence = self.sequence()
        highest_element = 2 ** self.degree - 1
        complement_pattern = sequence.index(highest_element)
        result = highest_element - complement_pattern

    return result
