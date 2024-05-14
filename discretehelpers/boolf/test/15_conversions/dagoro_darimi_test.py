from discretehelpers.boolf.examples import dagoro, darimi
from discretehelpers.sig_perm import SigPerm


def test():

    dagoro_clan = dagoro.ec_clan(5)
    darimi_clan = darimi.ec_clan()

    assert dagoro_clan.glove_compartment == darimi_clan.glove_compartment == [
        (0, 1, 2, 3),
        (0, 1, 2, 4),
        (0, 1, 3, 4),
        (0, 2, 3, 4),
        (1, 2, 3, 4)
    ]
    combos = dagoro_clan.glove_compartment

    # Each block contain only a single triple.
    am, an, ac = dagoro_clan.get_block_from_label(darimi)[0]
    bm, bn, bc = darimi_clan.get_block_from_label(dagoro)[0]

    assert (am, an, ac) == (1, 5, 4)
    assert (bm, bn, bc) == (4, 5, 0)

    signed_variation_a = SigPerm(pair=(am, an)).apply_on_vector(combos[ac])
    signed_variation_b = SigPerm(pair=(bm, bn)).apply_on_vector(combos[bc])

    assert signed_variation_a == (~3,  2,  1,  4)
    assert signed_variation_b == ( 2,  1, ~0,  3)

    assert dagoro.apply(*signed_variation_a) == darimi
    assert darimi.apply(*signed_variation_b) == dagoro
