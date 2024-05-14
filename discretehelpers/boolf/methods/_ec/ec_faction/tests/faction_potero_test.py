from itertools import product

from discretehelpers.boolf.examples import potero


a = potero.ec_faction()
b = potero.ec_faction(4)
c = potero.ec_faction(4, suppress_abbreviation=True)

labels_a = a.block_labels
labels_b = b.block_labels
labels_c = c.block_labels

domain_a = set(range(6))
domain_b = set(product(range(6), range(4)))
domain_c = set(range(24))


def test():

    from discretehelpers.set_part import SetPart
    from discretehelpers.boolf import Boolf

    assert a == SetPart([], domain_a)
    assert b == SetPart([], domain_b)
    assert c == SetPart([], domain_c)

    assert len(labels_a) == 6
    assert len(labels_b) == len(labels_c) == 24

    # no abbreviation necessary
    assert labels_a == {
        (0,): Boolf('1101 0001'),
        (1,): Boolf('1011 0001'),
        (2,): Boolf('1100 0101'),
        (3,): Boolf('1000 1101'),
        (4,): Boolf('1010 0011'),
        (5,): Boolf('1000 1011')
    }

    # abbreviated
    assert labels_b == {
        ((0, 0),): Boolf('1101 0001'),
        ((1, 0),): Boolf('1011 0001'),
        ((2, 0),): Boolf('1100 0101'),
        ((3, 0),): Boolf('1010 0011'),
        ((4, 0),): Boolf('1000 1101'),
        ((5, 0),): Boolf('1000 1011'),

        ((0, 1),): Boolf('1101 0001', [0, 1, 3]),
        ((1, 1),): Boolf('1011 0001', [0, 1, 3]),
        ((2, 1),): Boolf('1100 0101', [0, 1, 3]),
        ((3, 1),): Boolf('1010 0011', [0, 1, 3]),
        ((4, 1),): Boolf('1000 1101', [0, 1, 3]),
        ((5, 1),): Boolf('1000 1011', [0, 1, 3]),

        ((0, 2),): Boolf('1101 0001', [0, 2, 3]),
        ((1, 2),): Boolf('1011 0001', [0, 2, 3]),
        ((2, 2),): Boolf('1100 0101', [0, 2, 3]),
        ((3, 2),): Boolf('1010 0011', [0, 2, 3]),
        ((4, 2),): Boolf('1000 1101', [0, 2, 3]),
        ((5, 2),): Boolf('1000 1011', [0, 2, 3]),

        ((0, 3),): Boolf('1101 0001', [1, 2, 3]),
        ((1, 3),): Boolf('1011 0001', [1, 2, 3]),
        ((2, 3),): Boolf('1100 0101', [1, 2, 3]),
        ((3, 3),): Boolf('1010 0011', [1, 2, 3]),
        ((4, 3),): Boolf('1000 1101', [1, 2, 3]),
        ((5, 3),): Boolf('1000 1011', [1, 2, 3])
    }

    assert labels_c == {
        (0,): Boolf('1101 0001'),
        (1,): Boolf('1011 0001'),
        (2,): Boolf('1100 0101'),
        (3,): Boolf('1000 1101'),
        (4,): Boolf('1010 0011'),
        (5,): Boolf('1000 1011'),

        (6,): Boolf('1101 0001', [0, 1, 3]),
        (7,): Boolf('1011 0001', [0, 1, 3]),
        (8,): Boolf('1100 0101', [0, 1, 3]),
        (9,): Boolf('1000 1101', [0, 1, 3]),
        (10,): Boolf('1010 0011', [0, 1, 3]),
        (11,): Boolf('1000 1011', [0, 1, 3]),

        (12,): Boolf('1101 0001', [0, 2, 3]),
        (13,): Boolf('1011 0001', [0, 2, 3]),
        (14,): Boolf('1100 0101', [0, 2, 3]),
        (15,): Boolf('1000 1101', [0, 2, 3]),
        (16,): Boolf('1010 0011', [0, 2, 3]),
        (17,): Boolf('1000 1011', [0, 2, 3]),

        (18,): Boolf('1101 0001', [1, 2, 3]),
        (19,): Boolf('1011 0001', [1, 2, 3]),
        (20,): Boolf('1100 0101', [1, 2, 3]),
        (21,): Boolf('1000 1101', [1, 2, 3]),
        (22,): Boolf('1010 0011', [1, 2, 3]),
        (23,): Boolf('1000 1011', [1, 2, 3])
    }
