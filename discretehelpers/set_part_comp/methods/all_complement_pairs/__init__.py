def all_complement_pairs(self):

    from itertools import product

    pairs = set()

    for a, b in self.comp_pairs:
        block_a = self.get_block(a)
        block_b = self.get_block(b)
        pairs_a_b = product(block_a, block_b)
        for x, y in pairs_a_b:
            tuple_x_y = tuple(sorted([x, y]))
            pairs.add(tuple_x_y)

    return pairs
