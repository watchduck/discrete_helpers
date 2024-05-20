from discretehelpers.boolf.a import spread_sigperm_to_sigvar as apply_spread
from discretehelpers.boolf.examples import demole
from discretehelpers.sig_perm import SigPerm


x = demole.bloatless_boolf             # bloatless default     (C instead of A)
y = demole.filtrated_boolf([0, 1, 3])  # bloatless alternative (A instead of C)


def test_all():

    assert x.atomvals == [1, 2, 3]
    assert y.atomvals == [0, 1, 3]

    valency = x.valency  # 3

    x_root = x.root_boolf
    y_root = y.root_boolf

    x_clan = x_root.ec_clan()
    y_clan = y_root.ec_clan()

    block_a = x_clan.get_block_from_label(y_root)
    block_b = y_clan.get_block_from_label(x_root)

    assert block_a == [(1, 1), (1, 3), (2, 0), (2, 5), (4, 2), (4, 4)]
    assert block_b == [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5)]

    spread_x = x.spread_vector
    spread_y = y.spread_vector

    assert spread_x == [1, 1, 1]
    assert spread_y == [0, 0, 1]

    sigperms_a = [SigPerm(pair=_).sequence(valency) for _ in block_a]
    sigperms_b = [SigPerm(pair=_).sequence(valency) for _ in block_b]

    assert sigperms_a == [[1, ~0, 2], [2, ~0, 1], [0, ~1, 2], [2, ~1, 0], [0, ~2, 1], [1, ~2, 0]]
    assert sigperms_b == [[0, ~1, 2], [~1, 0, 2], [0, 2, ~1], [2, 0, ~1], [~1, 2, 0], [2, ~1, 0]]

    sigvars_a = [apply_spread(sigperm, spread_y) for sigperm in sigperms_a]
    sigvars_b = [apply_spread(sigperm, spread_x) for sigperm in sigperms_b]

    assert sigvars_a == [[1, ~0, 3], [3, ~0, 1], [0, ~1, 3], [3, ~1, 0], [0, ~3, 1], [1, ~3, 0]]  # 0, 1, 3
    assert sigvars_b == [[1, ~2, 3], [~2, 1, 3], [1, 3, ~2], [3, 1, ~2], [~2, 3, 1], [3, ~2, 1]]  # 1, 2, 3

    for i in range(len(block_a)):
        a = sigperms_a[i]
        b = sigperms_b[i]

        assert x.apply(*a) == y_root
        assert y.apply(*b) == x_root

        sigvar_a = sigvars_a[i]
        sigvar_b = sigvars_b[i]

        assert x.apply(*sigvar_a) == y
        assert y.apply(*sigvar_b) == x


def test_samples():
    assert x.apply(1, ~0, 3) == x.apply(0, ~3, 1) == y
    assert y.apply(1, ~2, 3) == y.apply(3, 1, ~2) == x
