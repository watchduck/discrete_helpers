from functools import cached_property


@cached_property
def is_blotless(self):

    return len(self.onesided_atomkeys) == 0
