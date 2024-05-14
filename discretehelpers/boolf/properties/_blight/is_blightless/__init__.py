from functools import cached_property


@cached_property
def is_blightless(self):

    return self.is_bloatless and self.is_blotless
