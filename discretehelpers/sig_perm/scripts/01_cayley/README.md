This script examines the product of elements of the
<a href="https://en.wikiversity.org/wiki/Full_octahedral_group">octahedral group</a> in pair notation.

(_pm_, _pn_) = (_am_, _an_) ∘ (_bm_, _bn_)

The move part simply from S<sub>4</sub>:

_pn_ = _an_ ∘ _bn_

Calculating the sign part involves the cube vertex permutation (property `schoute_perm`):

_pm_ = cvp(_am_, _an_)[_bm_]
