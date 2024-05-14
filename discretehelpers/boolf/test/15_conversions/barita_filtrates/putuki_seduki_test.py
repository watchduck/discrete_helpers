from discretehelpers.boolf.a import spread_sigperm_to_sigvar as apply_spread
from discretehelpers.boolf.examples import putuki, seduki
from discretehelpers.sig_perm import SigPerm


def test_all():

    valency = putuki.valency
    seduki_dense = seduki.dense_boolf
    
    putuki_clan = putuki.ec_clan()
    seduki_clan = seduki_dense.ec_clan()
    
    block_a = putuki_clan.get_block_from_label(seduki_dense)
    block_b = seduki_clan.get_block_from_label(putuki)

    assert block_a == block_b
    block = block_a

    assert block == [(0, 0), (0, 5), (0, 7), (0, 9), (0, 14), (0, 16), (0, 18), (0, 23)]

    spread = seduki.spread_vector
    assert spread == [0, 1, 1, 2]
    
    sigperms = [SigPerm(pair=_).sequence(valency) for _ in block]

    assert sigperms == [
        [0, 1, 2, 3], [2, 1, 0, 3], [1, 0, 3, 2], [3, 0, 1, 2], [0, 3, 2, 1], [2, 3, 0, 1], [1, 2, 3, 0], [3, 2, 1, 0]
    ]

    sigvars = [apply_spread(sigperm, spread) for sigperm in sigperms]  # signed variations
    assert sigvars == [
        [0, 2, 3, 5], [3, 2, 0, 5], [2, 0, 5, 3], [5, 0, 2, 3], [0, 5, 3, 2], [3, 5, 0, 2], [2, 3, 5, 0], [5, 3, 2, 0]
    ]
    
    for i in range(8):
    
        sigperm = sigperms[i]

        assert putuki.apply(*sigperm) == seduki_dense
        assert seduki.apply(*sigperm) == seduki_dense.apply(*sigperm) == putuki
    
        sigvar = sigvars[i]
        assert putuki.apply(*sigvar) == seduki


def test_samples():
    assert putuki.apply(0, 2, 3, 5) == putuki.apply(3, 5, 0, 2) == seduki
    assert seduki.apply(0, 1, 2, 3) == seduki.apply(2, 3, 0, 1) == putuki
