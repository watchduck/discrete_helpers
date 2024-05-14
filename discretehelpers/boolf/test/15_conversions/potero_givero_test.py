from discretehelpers.boolf.examples import potero, givero
from discretehelpers.sig_perm import SigPerm


def test():

    potero_clan = potero.ec_clan()
    givero_clan = givero.ec_clan()

    block_a = potero_clan.get_block_from_label(givero)
    block_b = givero_clan.get_block_from_label(potero)

    assert block_a == [(1, 4), (6, 2)]
    assert block_b == [(4, 3), (6, 2)]

    sigperms_a = [SigPerm(pair=_).sequence(3) for _ in block_a]
    sigperms_b = [SigPerm(pair=_).sequence(3) for _ in block_b]

    assert sigperms_a == [[1, 2, ~0], [0, ~2, ~1]]
    assert sigperms_b == [[~2, 0, 1], [0, ~2, ~1]]

    a0, a1 = sigperms_a
    b0, b1 = sigperms_b

    assert potero.apply(*a0) == potero.apply(*a1) == givero
    assert givero.apply(*b0) == givero.apply(*b1) == potero
