from discretehelpers.a import true_except, have


def _index(self, a):  # index of the block or None if singleton
    return self.equal_part.non_singleton_to_block_index_or_none(a)


def _exposet(self, a, b):  # index of each block or None if singleton
    return _index(self, a), _index(self, b)


def _representative(self, a):  # smallest element from the block
    return min(self.equal_part.element_to_block(a))


def _representatives(self, a, b):  # smallest elements from the blocks
    return _representative(self, a), _representative(self, b)


def _other_element_in_pair(pair, element):
    bucket = list(pair)
    bucket.remove(element)
    return bucket[0]


def _pair(a, b):
    return tuple(sorted([a, b]))
