from discretehelpers.a import true_except

from ...ex import DomainsNotEqualError


# This is a mere prototype.
def meet_pairs(self, other):

    from discretehelpers.set_part import SetPart

    true_except(self.domain == other.domain, DomainsNotEqualError)
    result = SetPart([], self.domain)
    for pair in self.pairs.intersection(other.pairs):
        result.merge_pair(*pair)
    return result


# This is used by the `join` method below.
def join_pairs(self, other):

    from discretehelpers.set_part import SetPart

    true_except(self.domain == other.domain, DomainsNotEqualError)
    result = SetPart([], self.domain)
    for pair in self.pairs.union(other.pairs):
        result.merge_pair(*pair)
    return result


def meet(self, other):

    from itertools import product
    from discretehelpers.set_part import SetPart

    meet_blocks = []
    for s_block, o_block in product(self.blocks, other.blocks):
        intersection = set(s_block) & set(o_block)
        if intersection:
            meet_blocks.append(sorted(intersection))

    return SetPart(meet_blocks, self.domain)


def join(self, other):

    from itertools import chain
    from discretehelpers.set_part import SetPart

    meet_part = self.meet(other)

    trash = set()
    rep_to_trash = dict()
    for block in meet_part.blocks:
        block_rep = min(block)
        block_trash = set(block) - {block_rep}
        trash |= block_trash
        rep_to_trash[block_rep] = block_trash

    clean_s_blocks = [sorted(set(block) - trash) for block in self.blocks]
    clean_o_blocks = [sorted(set(block) - trash) for block in other.blocks]

    clean_s_part = SetPart(clean_s_blocks)
    clean_o_part = SetPart(clean_o_blocks)

    clean_join_part = clean_s_part.join_pairs(clean_o_part)

    s_elements = set(chain.from_iterable(self.blocks))
    o_elements = set(chain.from_iterable(other.blocks))
    dirty_domain = s_elements | o_elements
    clean_domain = dirty_domain - trash

    dirty_join_blocks = []
    clean_blocks_with_singletons = clean_join_part.blocks_with_singletons(elements=clean_domain)
    for clean_block in clean_blocks_with_singletons:
        dirty_block = set(clean_block)
        for element in clean_block:
            if element in rep_to_trash:
                dirty_block |= rep_to_trash[element]
        dirty_join_blocks.append(sorted(dirty_block))

    return SetPart(dirty_join_blocks, domain=self.domain)
