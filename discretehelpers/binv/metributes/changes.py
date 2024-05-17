from functools import cached_property


@cached_property
def changes(self):
    """number of borders between runs of zeros and ones"""

    if self.length < 2:
        self.changes = 0
        return 0

    result = 0
    for i in range(1, self.length):
        if self[i - 1] != self[i]:
            result += 1

    return result
