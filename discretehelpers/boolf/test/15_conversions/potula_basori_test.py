from discretehelpers.boolf.examples import potula, basori
from discretehelpers.sig_perm import SigPerm


def test():

    potula_clan = potula.ec_clan(5)
    basori_clan = basori.ec_clan()

    block_a = potula_clan.get_block_from_label(basori)
    block_b = basori_clan.get_block_from_label(potula)

    assert potula_clan.glove_compartment == basori_clan.glove_compartment == [
        (0, 1, 2),
        (0, 1, 3),
        (0, 1, 4),
        (0, 2, 3),
        (0, 2, 4),
        (0, 3, 4),
        (1, 2, 3),
        (1, 2, 4),
        (1, 3, 4),
        (2, 3, 4)
    ]
    combos = potula_clan.glove_compartment

    assert block_a == [(0, 0, 5), (2, 5, 5)]
    assert block_b == [(0, 0, 0), (2, 5, 0)]

    am, an, ac = block_a[0]
    bm, bn, bc = block_b[0]
    signed_variation_a0 = SigPerm(pair=(am, an)).apply_on_vector(combos[ac])
    signed_variation_b0 = SigPerm(pair=(bm, bn)).apply_on_vector(combos[bc])
    assert signed_variation_a0 == (0, 3, 4)
    assert signed_variation_b0 == (0, 1, 2)

    am, an, ac = block_a[1]
    bm, bn, bc = block_b[1]
    signed_variation_a1 = SigPerm(pair=(am, an)).apply_on_vector(combos[ac])
    signed_variation_b1 = SigPerm(pair=(bm, bn)).apply_on_vector(combos[bc])
    assert signed_variation_a1 == ( 4, ~3,  0)
    assert signed_variation_b1 == ( 2, ~1,  0)

    assert potula.apply(*signed_variation_a0) == potula.apply(*signed_variation_a1) == basori
    assert basori.apply(*signed_variation_b0) == basori.apply(*signed_variation_b1) == potula
