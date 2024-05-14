def __lt__(self, other):
    return self.vector < other.vector


def __gt__(self, other):
    return other < self


def __le__(self, other):
    return self == other or self < other


def __ge__(self, other):
    return other <= self
