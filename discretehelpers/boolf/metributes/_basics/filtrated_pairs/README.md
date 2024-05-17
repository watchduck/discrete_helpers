To each pair of atoms corresponds a small filtrate of the Boolf (compare [`filtrated_boolf`](../../methods/filtrated_boolf)).

Each filtrate is represented by a binary string of length 4.

* `1111` crossing
* `0111` universal (i.e. everything is in the union)
* `1011` subset
* `1101` superset 
* `1110` disjoint (i.e. nothing is in the intersection)

For a bloated Boolf also:
* `0110` complementary
* `1001` equal

The example in the test file is *tokosi*.
(See [here](https://en.wikiversity.org/wiki/Studies_of_Euler_diagrams/bloated#tokosi) for its diagram.)

Usually tested using the wrapper
[`filtrated_pairs_pretty`](../../methods/_pretty/filtrated_pairs_pretty).

The method [`filtrated_pair`](../../../methods/filtrated_pair) is a wrapper, which allows to ignore the pair's order.

Compare [`spot_atoms`](../_obsolete/spot_atoms).

The methods
[`atom_pair_subset`](../../methods/atom_pair_subset) 
and 
[`atom_pair_intersect`](../../methods/atom_pair_intersect)
are shorthands using this metribute.