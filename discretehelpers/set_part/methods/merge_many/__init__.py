from itertools import combinations


def merge_many(self, many):
    for a, b in combinations(many, 2):
        self.merge_pair(a, b)

    self.__init__(self.blocks, self.domain, self.block_labels)  # reinitialize
