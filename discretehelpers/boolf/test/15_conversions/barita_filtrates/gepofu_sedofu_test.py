from discretehelpers.boolf.a import spread_sigperm_to_sigvar as apply_spread
from discretehelpers.boolf.examples import gepofu, sedofu
from discretehelpers.sig_perm import SigPerm


def test_all():

    valency = gepofu.valency
    sedofu_root = sedofu.root_boolf

    gepofu_clan = gepofu.ec_clan()
    sedofu_clan = sedofu_root.ec_clan()
    
    block_a = gepofu_clan.get_block_from_label(sedofu_root)
    block_b = sedofu_clan.get_block_from_label(gepofu)
    
    assert block_a == [(0, 3), (0, 5), (0, 9), (0, 11), (0, 12), (0, 14), (0, 18), (0, 20)]
    assert block_b == [(0, 4), (0, 5), (0, 8), (0, 9), (0, 14), (0, 15), (0, 18), (0, 19)]
    
    spread = sedofu.spread_vector
    assert spread == [1, 1, 2, 2]
    
    sigperms_a = [SigPerm(pair=_).sequence(valency) for _ in block_a]
    sigperms_b = [SigPerm(pair=_).sequence(valency) for _ in block_b]
    
    assert sigperms_a == [
        [2, 0, 1, 3], [2, 1, 0, 3], [3, 0, 1, 2], [3, 1, 0, 2], [0, 2, 3, 1], [0, 3, 2, 1], [1, 2, 3, 0], [1, 3, 2, 0]
    ]
    assert sigperms_b == [
        [1, 2, 0, 3], [2, 1, 0, 3], [0, 3, 1, 2], [3, 0, 1, 2], [0, 3, 2, 1], [3, 0, 2, 1], [1, 2, 3, 0], [2, 1, 3, 0]
    ]
    
    sigvars_a = [apply_spread(sigperm, spread) for sigperm in sigperms_a]
    assert sigvars_a == [
        [4, 1, 2, 5], [4, 2, 1, 5], [5, 1, 2, 4], [5, 2, 1, 4], [1, 4, 5, 2], [1, 5, 4, 2], [2, 4, 5, 1], [2, 5, 4, 1]
    ]
    
    for i in range(len(block_a)):
    
        a = sigperms_a[i]
        b = sigperms_b[i]
    
        assert gepofu.apply(*a) == sedofu_root
        assert sedofu.apply(*b) == sedofu_root.apply(*b) == gepofu
    
        sigvar = sigvars_a[i]
        assert gepofu.apply(*sigvar) == sedofu


def test_samples():
    assert gepofu.apply(4, 1, 2, 5) == gepofu.apply(2, 5, 4, 1) == sedofu
    assert sedofu.apply(1, 2, 0, 3) == sedofu.apply(2, 1, 3, 0) == gepofu
