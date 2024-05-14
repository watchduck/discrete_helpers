class TooManyOverlapsERROR(Exception):
    """The two splits should have only 3 overlaps, but appear to have 4."""


class SmallerThanSelfERROR(Exception):
    """The gapless function must be true in the same or more spots."""
