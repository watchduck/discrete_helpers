from discretehelpers.binv import Binv
from discretehelpers.binv.a import binary_length


def int_matches(self, intval):

    intval_length = binary_length(intval)
    min_length = self.number_of_related_blocks()
    length = intval_length if intval_length > min_length else min_length
    binv = Binv(intval=intval, length=length)

    for equality_block in self.equal_part.blocks:
        equal_values = [binv.has_index(_) for _ in equality_block]
        should_be_one_value = set(equal_values)
        if not len(should_be_one_value) == 1:
            return False
    for comp_pair in self.comp_pairs:
        comp_values = [binv.has_index(_) for _ in comp_pair]
        should_be_two_values = set(comp_values)
        if not len(should_be_two_values) == 2:
            return False
    return True
