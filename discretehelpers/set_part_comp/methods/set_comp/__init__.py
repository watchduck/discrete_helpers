from discretehelpers.a import true_except, have

from ...helpers import _representative, _representatives, _pair
from ...ex import *


def set_comp(self, a, b):
    true_except(not self.are_equal(a, b), SetCompEqualsError)
    if self.are_comp(a, b):
        return  # nothing to do

    a_comp = self.get_comp(a)
    b_comp = self.get_comp(b)
    if not have(a_comp) and not have(b_comp):
        _set_comp_no_comp(self, a, b)
    elif not have(a_comp) and have(b_comp):
        _set_comp_first_comp(self, b, a, b_comp)
    elif have(a_comp) and not have(b_comp):
        _set_comp_first_comp(self, a, b, a_comp)
    elif have(a_comp) and have(b_comp):
        _set_comp_both_comp(self, a, b, a_comp, b_comp)


def _set_comp_no_comp(self, a, b):
    a_repr, b_repr = _representatives(self, a, b)
    self.comp_pairs.add(_pair(a_repr, b_repr))


def _set_comp_first_comp(self, a, b, a_comp):
    old_a_repr = _representative(self, a)
    self.comp_pairs.remove(_pair(old_a_repr, a_comp))  # remove old complement pair
    self.equal_part.merge_pair(a_comp, b)  # both are complements of `a`, thus equal
    new_a_repr, new_b_repr = _representatives(self, a, b)
    self.comp_pairs.add(_pair(new_a_repr, new_b_repr))  # add new complement pair


def _set_comp_both_comp(self, a, b, a_comp, b_comp):
    old_a_repr, old_b_repr = _representatives(self, a, b)

    # remove old complement pairs
    self.comp_pairs.remove(_pair(old_a_repr, a_comp))
    self.comp_pairs.remove(_pair(old_b_repr, b_comp))

    # merge blocks
    self.equal_part.merge_pair(a, b_comp)
    self.equal_part.merge_pair(b, a_comp)

    new_repr, new_comp_repr = _representatives(self, a, a_comp)
    self.comp_pairs.add(_pair(new_repr, new_comp_repr))  # add new complement pair
