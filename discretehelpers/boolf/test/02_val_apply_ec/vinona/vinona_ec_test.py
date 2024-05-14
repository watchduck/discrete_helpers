from discretehelpers.set_part import SetPart
from discretehelpers.sig_perm import SigPerm
from discretehelpers.boolf import Boolf
from discretehelpers.boolf.examples import vinona


def blocks_to_domain(blocks):
    domain = set()
    for block in blocks:
        for item in block:
            domain.add(item)
    return domain


blocks_2ary = [
        [(0, 0), (0, 1)],
        [(1, 0), (1, 1)],
        [(2, 0), (2, 1)],
        [(3, 0), (3, 1)]
    ]
domain_2ary = blocks_to_domain(blocks_2ary)


blocks_3ary_triples = [
    [(0, 0, 0), (0, 1, 0)], [(0, 0, 1), (0, 1, 1)], [(0, 0, 2), (0, 1, 2)], [(1, 0, 0), (2, 1, 0)],
    [(1, 0, 1), (2, 1, 1)], [(1, 0, 2), (2, 1, 2)], [(1, 1, 0), (2, 0, 0)], [(1, 1, 1), (2, 0, 1)],
    [(1, 1, 2), (2, 0, 2)], [(3, 0, 0), (3, 1, 0)], [(3, 0, 1), (3, 1, 1)], [(3, 0, 2), (3, 1, 2)]
]
domain_3ary_triples = blocks_to_domain(blocks_3ary_triples)


blocks_3ary_pairs = [
        [(0, 0), (0, 1), (4, 0), (4, 1)],
        [(0, 2), (0, 3), (2, 2), (2, 3)],
        [(0, 4), (0, 5), (1, 4), (1, 5)],
        [(1, 0), (1, 1), (5, 0), (5, 1)],
        [(1, 2), (1, 3), (3, 2), (3, 3)],
        [(2, 0), (2, 1), (6, 0), (6, 1)],
        [(2, 4), (2, 5), (3, 4), (3, 5)],
        [(3, 0), (3, 1), (7, 0), (7, 1)],
        [(4, 2), (4, 3), (6, 2), (6, 3)],
        [(4, 4), (4, 5), (5, 4), (5, 5)],
        [(5, 2), (5, 3), (7, 2), (7, 3)],
        [(6, 4), (6, 5), (7, 4), (7, 5)]
    ]
domain_3ary_pairs = blocks_to_domain(blocks_3ary_pairs)


########################################################################################################################


def test_2ary():

    family = vinona.ec_family()
    assert family == SetPart([], {0, 1, 2, 3})  # only singletons

    assert family.block_labels == {
        (0,): Boolf('1110'),
        (1,): Boolf('1101'),
        (2,): Boolf('1011'),
        (3,): Boolf('0111')
    }

    ###################################

    clan = vinona.ec_clan()
    assert clan == SetPart(blocks_2ary, domain_2ary)

    assert clan.block_labels == {
        ((0, 0), (0, 1)): Boolf('1110'),
        ((1, 0), (1, 1)): Boolf('1101'),
        ((2, 0), (2, 1)): Boolf('1011'),
        ((3, 0), (3, 1)): Boolf('0111')
    }

    assert clan.get_block_from_label(Boolf('1011')) == [(2, 0), (2, 1)]
    assert clan.get_label_from_element((2, 1)) == Boolf('1011')


########################################################################################################################


example_boolf = Boolf('1011', [0, 2])

sigperm_4_2 = SigPerm(pair=[4, 2])  # [ 0, ~2,  1]
sigperm_4_3 = SigPerm(pair=[4, 3])  # [~2,  0,  1]
sigperm_6_2 = SigPerm(pair=[6, 2])  # [ 0, ~2, ~1]
sigperm_6_3 = SigPerm(pair=[6, 3])  # [~2,  0, ~1]


def test_3ary_pairs():

    clan = vinona.ec_clan(3, suppress_abbreviation=True)

    assert clan == SetPart(blocks_3ary_pairs, domain_3ary_pairs)

    assert clan.block_labels == {
        ((0, 0), (0, 1), (4, 0), (4, 1)): Boolf('1110'),
        ((1, 0), (1, 1), (5, 0), (5, 1)): Boolf('1101'),
        ((2, 0), (2, 1), (6, 0), (6, 1)): Boolf('1011'),
        ((3, 0), (3, 1), (7, 0), (7, 1)): Boolf('0111'),

        ((0, 2), (0, 3), (2, 2), (2, 3)): Boolf('1110', [0, 2]),
        ((1, 2), (1, 3), (3, 2), (3, 3)): Boolf('1101', [0, 2]),
        ((4, 2), (4, 3), (6, 2), (6, 3)): Boolf('1011', [0, 2]),
        ((5, 2), (5, 3), (7, 2), (7, 3)): Boolf('0111', [0, 2]),

        ((0, 4), (0, 5), (1, 4), (1, 5)): Boolf('1110', [1, 2]),
        ((2, 4), (2, 5), (3, 4), (3, 5)): Boolf('1101', [1, 2]),
        ((4, 4), (4, 5), (5, 4), (5, 5)): Boolf('1011', [1, 2]),
        ((6, 4), (6, 5), (7, 4), (7, 5)): Boolf('0111', [1, 2])
    }

    assert clan.get_block_from_label(example_boolf) == [(4, 2), (4, 3), (6, 2), (6, 3)]
    assert clan.get_label_from_element((6, 2)) == example_boolf

    assert vinona.apply_sigperm(sigperm_4_2) == vinona.apply_sigperm(sigperm_6_2) == vinona.apply(0, ~2) \
        == vinona.apply_sigperm(sigperm_4_3) == vinona.apply_sigperm(sigperm_6_3) == vinona.apply(~2, 0) \
        == example_boolf


def test_3ary_triples():

    clan = vinona.ec_clan(3)

    assert clan == SetPart(blocks_3ary_triples, domain_3ary_triples)

    # The third entry in the triples is the key to this list of atomvals.
    assert clan.glove_compartment == [(0, 1), (0, 2), (1, 2)]

    assert clan.block_labels == {
        ((0, 0, 0), (0, 1, 0)): Boolf('1110'),
        ((1, 0, 0), (2, 1, 0)): Boolf('1101'),
        ((1, 1, 0), (2, 0, 0)): Boolf('1011'),
        ((3, 0, 0), (3, 1, 0)): Boolf('0111'),

        ((0, 0, 1), (0, 1, 1)): Boolf('1110', [0, 2]),
        ((1, 0, 1), (2, 1, 1)): Boolf('1101', [0, 2]),
        ((1, 1, 1), (2, 0, 1)): Boolf('1011', [0, 2]),
        ((3, 0, 1), (3, 1, 1)): Boolf('0111', [0, 2]),

        ((0, 0, 2), (0, 1, 2)): Boolf('1110', [1, 2]),
        ((1, 0, 2), (2, 1, 2)): Boolf('1101', [1, 2]),
        ((1, 1, 2), (2, 0, 2)): Boolf('1011', [1, 2]),
        ((3, 0, 2), (3, 1, 2)): Boolf('0111', [1, 2])
    }

    assert clan.get_block_from_label(example_boolf) == [(1, 1, 1), (2, 0, 1)]
    assert clan.get_label_from_element((2, 0, 1)) == example_boolf
