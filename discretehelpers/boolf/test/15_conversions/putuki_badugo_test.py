from discretehelpers.boolf.examples import putuki, badugo
from discretehelpers.sig_perm import SigPerm


def test_all():

    putuki_clan = putuki.ec_clan()
    badugo_clan = badugo.ec_clan()

    block_a = putuki_clan.get_block_from_label(badugo)
    block_b = badugo_clan.get_block_from_label(putuki)

    assert block_a == [(1, 0), (1, 5), (1, 7), (1, 9), (1, 14), (1, 16), (1, 18), (1, 23)]
    assert block_b == [(1, 0), (1, 14), (2, 7), (2, 18), (4, 5), (4, 16), (8, 9), (8, 23)]

    sigperms_a = [SigPerm(pair=_).sequence(4) for _ in block_a]
    sigperms_b = [SigPerm(pair=_).sequence(4) for _ in block_b]

    assert sigperms_a == [[~0, 1, 2, 3], [2, 1, ~0, 3], [1, ~0, 3, 2], [3, ~0, 1, 2], [~0, 3, 2, 1], [2, 3, ~0, 1], [1, 2, 3, ~0], [3, 2, 1, ~0]]  # val 0 negated
    assert sigperms_b == [[~0, 1, 2, 3], [~0, 3, 2, 1], [~1, 0, 3, 2], [~1, 2, 3, 0], [~2, 1, 0, 3], [~2, 3, 0, 1], [~3, 0, 1, 2], [~3, 2, 1, 0]]  # key 0 negated

    for i in range(8):
        a = sigperms_a[i]
        b = sigperms_b[i]
        assert putuki.apply(*a) == badugo
        assert badugo.apply(*b) == putuki


def test_samples():
    assert putuki.apply(~0, 1, 2, 3) == putuki.apply(3, 2, 1, ~0) == badugo
    assert badugo.apply(~0, 1, 2, 3) == badugo.apply(~3, 2, 1, 0) == putuki
