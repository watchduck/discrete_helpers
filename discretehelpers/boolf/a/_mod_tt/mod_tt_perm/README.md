# permute truth table

This helper function is similar to the `Boolf` methods `apply` or `apply_sigperm`.<br>
It avoids the `Boolf` class, and uses [`WalshPerm`](../../../walsh_perm) for the permutation.

It allows truth tables of inflated Boolean functions.<br>
E.g. `mod_tt_perm(Binv('1111 1010'), [1, 2, 0])` is `Binv('1110 1110')`.

Using the `Boolf` class would lead to the complication,<br>
that `Boolf('1111 1010')` gets deflated to `Boolf('1110', [0, 2])`.

**Introduced inverse!**