from itertools import chain

from discretehelpers.a import have, true_except
from discretehelpers.ex import ArgValueError, ArgTypeError


def refine_block(self, new_blocks, new_labels=None):

    true_except(type(new_blocks) in [list, tuple], ArgTypeError)

    old_block = sorted(chain(*new_blocks))
    
    combined_length_of_new_blocks = sum([len(_) for _ in new_blocks])
    true_except(combined_length_of_new_blocks == len(old_block), ArgValueError)  # check if blocks do not overlap

    true_except(old_block in self.blocks, ArgValueError)

    self.blocks.remove(old_block)
    self.blocks += new_blocks

    try:  # The old block may have a label. If so, delete it. If not, do nothing.
        del self.block_labels[tuple(old_block)]
    except KeyError:
        pass

    if have(new_labels):
        true_except(type(new_labels) in [list, tuple], ArgTypeError)
        true_except(len(new_labels) == len(new_blocks), ArgValueError)
        for i, block in enumerate(new_blocks):
            label = new_labels[i]
            self.block_labels[tuple(block)] = label

    self.__init__(self.blocks, self.domain, self.block_labels)  # reinitialize
