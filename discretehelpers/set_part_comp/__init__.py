from discretehelpers.a import have


from discretehelpers.set_part import SetPart

from .helpers import _exposet, _representatives, _other_element_in_pair, _pair
from .ex import *


class SetPartComp():

    def __init__(self, equal_part=None, comp_pairs=None):
        if not have(equal_part) and have(comp_pairs):
            raise CompWithoutPartError

        if have(equal_part):
            if type(equal_part) == list:
                self.equal_part = SetPart(equal_part, 'Z')
            elif type(equal_part) == SetPart:
                self.equal_part = equal_part
        else:
            self.equal_part = SetPart([], 'Z')

        if have(comp_pairs):
            canonical_comp_pairs = set()
            for a, b in comp_pairs:
                canonical_a = min(self.equal_part.element_to_block(a))
                canonical_b = min(self.equal_part.element_to_block(b))
                canonical_pair = tuple(sorted([canonical_a, canonical_b]))
                canonical_comp_pairs.add(canonical_pair)
            self.comp_pairs = canonical_comp_pairs
        else:
            self.comp_pairs = set()

        if have(equal_part) and have(comp_pairs):  # check if arguments do not contradict each other
            for pair in self.comp_pairs:
                if self.equal_part.pair_in_same_block(*pair):
                    raise PartCompMismatchError

    from .methods import set_equal, set_comp, boolf, int_matches, all_complement_pairs

    def are_equal(self, a, b):
        a_index, b_index = _exposet(self, a, b)
        if not (have(a_index) and have(b_index)):
            return False
        return a_index == b_index

    def are_comp(self, a, b):
        a_repr, b_repr = _representatives(self, a, b)
        return _pair(a_repr, b_repr) in self.comp_pairs

    def get_comp(self, element):  # smallest element of the complementary block (if any, else None)
        for some_pair in self.comp_pairs:
            for some_elm in some_pair:
                some_block = self.equal_part.element_to_block(some_elm)
                if element in some_block:
                    return _other_element_in_pair(some_pair, some_elm)
        return None

    def get_block(self, element):  # whole block of equivalents to element
        if element in self.equal_part.non_singletons:
            return self.equal_part.element_to_block(element)
        else:
            return [element]

    def get_repr(self, element):  # smallest element of the block that contains the element
        return min(self.get_block(element))

    def __eq__(self, other):
        return self.equal_part == other.equal_part and self.comp_pairs == other.comp_pairs

    def __str__(self):
        blocks = self.equal_part.blocks
        pairs = self.comp_pairs
        if len(pairs):
            return f'SetPartComp({blocks}, {pairs})'
        else:
            return f'SetPartComp({blocks})'

    def __repr__(self):
        return self.__str__()

    def related_part(self):  # set partition with complementary blocks merged
        part = SetPart(self.equal_part.blocks, 'Z')
        for a, b in self.comp_pairs:
            part.merge_pair(a, b)
        return part

    def number_of_related_blocks(self):
        return len(self.related_part().blocks)

    def length(self):
        return max(self.related_part().non_singletons) + 1  # not `related_part().length`, because its domain is Z

    def affected_elements(self):
        elements = set()
        for block in self.related_part().blocks:
            elements = elements.union(set(block))
        return sorted(elements)

    def number_of_affected_elements(self):
        return len(self.affected_elements())
