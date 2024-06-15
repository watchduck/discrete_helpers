from discretehelpers.a import true_except

from ...ex import DomainsNotEqualError


def _meet_prototype(self, other):

    from discretehelpers.set_part import SetPart

    true_except(self.domain == other.domain, DomainsNotEqualError)

    result = SetPart([], self.domain)
    for pair in self.pairs.intersection(other.pairs):
        result.merge_pair(*pair)
    return result


def meet(self, other):

    from itertools import product
    from discretehelpers.set_part import SetPart

    true_except(self.domain == other.domain, DomainsNotEqualError)

    meet_blocks = []
    for s_block, o_block in product(self.blocks, other.blocks):
        intersection = set(s_block) & set(o_block)
        if intersection:
            meet_blocks.append(sorted(intersection))

    return SetPart(meet_blocks, self.domain)
