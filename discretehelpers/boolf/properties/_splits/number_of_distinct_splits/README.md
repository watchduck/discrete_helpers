The number of distinct splits is the length of
[`splits_equality_blocks`, `splits_preferred_side`](../splits_eq_blocks_and_pref_side)
and
[`bloatless_atomkeys_undeflated`](../bloatless_atomkeys_undeflated).

It is not technically the number of distinct entries of [`splits`](../splits),
because these entries are stored as ordered pairs (set first, complement last).
The actual splits are the unordered equivalents of these pairs.

This is usually equal to the valency of the [`bloatless_boolf`](../bloatless_boolf),
but there are cases when this valency is smaller.
See example [there](../bloatless_boolf).
