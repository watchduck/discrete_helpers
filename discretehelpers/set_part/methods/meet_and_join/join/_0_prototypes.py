from discretehelpers.a import true_except

from ....ex import DomainsNotEqualError


# used by `_join_prototype_improved`
def _join_prototype(self, other):

    from discretehelpers.set_part import SetPart

    true_except(self.domain == other.domain, DomainsNotEqualError)
    result = SetPart([], self.domain)
    for pair in self.pairs.union(other.pairs):
        result.merge_pair(*pair)
    return result


def _join_prototype_improved(self, other):

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

    clean_join_part = clean_s_part._join_prototype(clean_o_part)

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
