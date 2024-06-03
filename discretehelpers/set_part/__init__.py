from bidict import bidict

from discretehelpers.a import true_except, is_natural, have

from .ex import DomainsNotEqualError, DomainNotSetLikeError, DuplicateElementsError


class SetPart(object):

    def __init__(self, blocks=None, domain='N', block_labels=None):

        if domain not in ['N', 'Z']:
            true_except(type(domain) in [set, list, tuple, range], DomainNotSetLikeError)
            self.domain = set(domain)
        else:
            self.domain = domain  # keep the letters

        if blocks is None:
            self.set_trivial()
            return

        blocks = sorted(sorted(block) for block in blocks if len(block) > 1)
        if not blocks:
            self.set_trivial()
            return

        self.blocks = blocks

        _ = dict()
        for block_index, block in enumerate(self.blocks):
            for element in block:
                _[element] = block_index
        self.non_singleton_to_block_index = _

        self.non_singletons = set(self.non_singleton_to_block_index.keys())
        true_except(
            len(self.non_singletons) == sum([len(block) for block in self.blocks]),
            DuplicateElementsError
        )

        if self.domain == 'N':
            self.length = max(self.non_singletons) + 1

        self.trivial = False

        if have(block_labels):
            self.block_labels = bidict(block_labels)
        else:
            self.block_labels = bidict()  # remains empty until filled with `add_block_label`

        self.set_dummies()

    from .metributes import pairs, intval, canonical_blocks_with_singletons, singletons

    from .methods.blocks_with_singletons import blocks_with_singletons
    from .methods.merge_pair import merge_pair
    from .methods.merge_many import merge_many
    from .methods.block_labels import add_label_to_block, add_label_to_element, \
        get_label_from_block, get_label_from_element, get_block_from_label, get_block_from_element, merge_block_labels
    from .methods.refine_block import refine_block
    from .methods.meet_and_join import meet, join, meet_pairs, join_pairs

    def set_trivial(self):
        self.trivial = True
        self.blocks = []
        self.non_singleton_to_block_index = dict()
        self.non_singletons = set()
        self.block_labels = bidict()

        if self.domain == 'N':
            self.length = 0

        self.set_dummies()

    def set_dummies(self):
        self._pairs = None
        self._intval = None
        self._canonical_blocks_with_singletons = None
        self._singletons = None
        self.glove_compartment = None  # just a handy stowaway (without functionality within this class)

    def __eq__(self, other):
        true_except(self.domain == other.domain, DomainsNotEqualError)
        return self.blocks == other.blocks

    def __str__(self):
        if self.domain == 'N':
            return 'SetPart(' + str(self.blocks) + ')'
        elif self.domain == 'Z':
            return 'SetPart(' + str(self.blocks) + ", 'Z')"
        else:
            sorted_domain = sorted(self.domain)
            sorted_domain_string = ', '.join([str(_) for _ in sorted_domain])
            return 'SetPart(' + str(self.blocks) + ', {' + sorted_domain_string + '})'

    def __repr__(self):
        return self.__str__()

    def non_singleton_to_block_index_or_none(self, element):
        if element in self.non_singletons:
            return self.non_singleton_to_block_index[element]
        else:
            return None

    def pair_in_same_block(self, a, b):
        if not {a, b}.issubset(self.non_singletons):
            return False
        return self.non_singleton_to_block_index[a] == self.non_singleton_to_block_index[b]

    def element_to_block(self, element):
        if element in self.non_singletons:
            return self.blocks[self.non_singleton_to_block_index[element]]
        else:
            return [element]

    def element_in_domain(self, element):
        if self.domain == 'N':
            return is_natural(element)
        elif self.domain == 'Z':
            return type(element) == int
        else:
            return element in self.domain

    def __le__(self, other):
        true_except(self.domain == other.domain, DomainsNotEqualError)
        return self.join(other) == other

    def __lt__(self, other):
        return self != other and self <= other
