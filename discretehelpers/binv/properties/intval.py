from functools import cached_property


@cached_property
def intval(self):

    if self.string == '':
        result = 0
    else:
        result = int(self.string[::-1], 2)

    return result
