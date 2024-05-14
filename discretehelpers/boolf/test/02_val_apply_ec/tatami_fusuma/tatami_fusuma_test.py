from discretehelpers.a import int_to_perm
from discretehelpers.boolf import Boolf
from discretehelpers.boolf.examples import tatami, fusuma, geloba


def test_faction():

    tatami_faction = tatami.ec_faction()
    assert tatami_faction.block_labels == {
        (0, 1): Boolf('1111 1000'),
        (2, 3): Boolf('1110 1100'),
        (4, 5): Boolf('1110 1010')
    }

    fusuma_faction = fusuma.ec_faction()
    assert fusuma_faction.block_labels == {
        (0,): Boolf('1111 0100'),
        (1,): Boolf('1111 0010'),
        (2,): Boolf('1101 1100'),
        (3,): Boolf('1100 1110'),
        (4,): Boolf('1011 1010'),
        (5,): Boolf('1010 1110')
    }
    perm_3 = int_to_perm(3)
    assert fusuma.apply_sigperm(perm_3) == Boolf('1100 1110')


def test_family():
    tatami_family = tatami.ec_family()
    assert tatami_family.block_labels == {
        (0,): Boolf('1111 1000'),
        (1,): Boolf('1111 0100'),  # fusuma
        (2,): Boolf('1111 0010'),
        (3,): Boolf('1111 0001'),
        (4,): Boolf('1000 1111'),  # geloba
        (5,): Boolf('0100 1111'),
        (6,): Boolf('0010 1111'),
        (7,): Boolf('0001 1111')
    }

    fusuma_family = fusuma.ec_family()
    assert fusuma_family.block_labels == {
        (0,): Boolf('1111 0100'),
        (1,): Boolf('1111 1000'),  # tatami
        (2,): Boolf('1111 0001'),
        (3,): Boolf('1111 0010'),
        (4,): Boolf('0100 1111'),
        (5,): Boolf('1000 1111'),  # geloba
        (6,): Boolf('0001 1111'),
        (7,): Boolf('0010 1111')
    }

    assert fusuma_family.get_block_from_label(fusuma) == [0]
    assert fusuma_family.get_block_from_label(tatami) == [1]
    assert fusuma_family.get_block_from_label(geloba) == [5]

    assert fusuma.apply_sigperm([~0, 1, 2]) == tatami
    assert fusuma.apply_sigperm([~0, 1, ~2]) == geloba
