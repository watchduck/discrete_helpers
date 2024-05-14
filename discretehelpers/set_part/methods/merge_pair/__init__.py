from discretehelpers.a import true_except

from ...ex import NotInDomainError
from ...methods.block_labels.ex import LabelContradictionError


def merge_pair(self, a, b):

    if a == b:
        return  # nothing to do

    true_except(self.element_in_domain(a) and self.element_in_domain(b), NotInDomainError)

    try:
        self.merge_block_labels(a, b)
    except LabelContradictionError:
        raise LabelContradictionError  # stop

    a_found = a in self.non_singletons
    b_found = b in self.non_singletons

    if a_found and b_found:

        block_index_a = self.non_singleton_to_block_index[a]
        block_index_b = self.non_singleton_to_block_index[b]

        if block_index_a == block_index_b:
            return  # nothing to do

        block_a = self.blocks[block_index_a]
        block_b = self.blocks[block_index_b]
        merged_block = sorted(block_a + block_b)

        self.blocks.remove(block_a)
        self.blocks.remove(block_b)
        self.blocks.append(merged_block)

    elif not a_found and not b_found:
        self.blocks.append([a, b])

    else:  # a_found and not b_found
        if b_found and not a_found:
            a, b = b, a
        block_index_a = self.non_singleton_to_block_index[a]
        self.blocks[block_index_a].append(b)

    self.__init__(self.blocks, self.domain, self.block_labels)  # reinitialize
