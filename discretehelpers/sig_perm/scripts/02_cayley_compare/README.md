This script checks that `SetPerm` objects and two corresponding objects really form the Cayley table.

The example is the <a href="https://en.wikiversity.org/wiki/Full_octahedral_group">octahedral group</a>,
just like in the last script.

The corresponding objects are the 3×3 signed permutation matrices (`matrix(3)`)<br>
and the cube vertex permutations (`schoute_perm`), which are `Perm` objects with period length 8.