# splits equality blocks and preferred side

The metributes `splits_equality_blocks` and `splits_preferred_side` are lists with corresponding entries,
and are calculated together.

If a block contains complements, 
then the corresponding entry in `splits_preferred_side` denotes the preferred side.
It will be treated as the set (recto), and the other one as the complement (verso).

If the block does not contain complements, the corresponding entry in `splits_preferred_side` is `None`.

The entries of each block are atomkeys, i.e. they are keys to `splits`.
To say that they are complementary means, that the corresponding entries of `splits` are,
which means that the split's recto and verso (first and second set in the pair) are exchanged.

These metributes are calculated together, because the choice of preferred sides can change the order of both.
(That is the use of `sort_together` based on the `representative_atomkeys` at the end.)

For examples see [test/05_blight](../../../test/05_blight/bloat/preferred_side).
