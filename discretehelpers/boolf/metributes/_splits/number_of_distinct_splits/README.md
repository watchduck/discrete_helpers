# number of distinct splits

This is the length of
[`splits_equality_blocks`](../splits_eq_blocks_and_pref_side)
and
[`bloatless_atomkeys_undeflated`](../../_blight/bloatless_atomkeys_undeflated).

It is not technically the number of distinct entries of [`splits`](../splits),
because these entries are stored as ordered pairs (_recto_, _verso_).
The actual splits are the unordered equivalents of these pairs.

This is usually equal to the valency of the [`bloatless_boolf`](../../_blight/bloatless_boolf). (See there for the counterexample *bareto*.)
