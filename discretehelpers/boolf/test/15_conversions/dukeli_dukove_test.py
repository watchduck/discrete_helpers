from discretehelpers.boolf.examples import dukeli, dukove
from discretehelpers.sig_perm import SigPerm


def test():

    dukeli_clan = dukeli.ec_clan()
    dukove_clan = dukove.ec_clan()

    block_a = dukeli_clan.get_block_from_label(dukove)
    block_b = dukove_clan.get_block_from_label(dukeli)

    assert block_a == [(0, 3), (0, 11)]
    assert block_b == [(0, 4), (0, 19)]

    sigperms_a = [SigPerm(pair=_).sequence(4) for _ in block_a]
    sigperms_b = [SigPerm(pair=_).sequence(4) for _ in block_b]

    assert sigperms_a == [[2, 0, 1, 3], [3, 1, 0, 2]]
    assert sigperms_b == [[1, 2, 0, 3], [2, 1, 3, 0]]

    a0, a1 = sigperms_a
    b0, b1 = sigperms_b

    assert dukeli.apply(*a0) == dukeli.apply(*a1) == dukove
    assert dukove.apply(*b0) == dukove.apply(*b1) == dukeli
