from itertools import product

from discretehelpers.set_part import SetPart


def test():

    from discretehelpers.boolf import Boolf

    boolf = Boolf('0110 1001')

    a = boolf.ec_faction()
    b = boolf.ec_faction(4)
    c = boolf.ec_faction(4, suppress_abbreviation=True)

    ####################################################################################################################

    domain_6 = set(range(6))
    domain_6x4 = set(product(range(6), range(4)))
    domain_24 = set(range(24))

    assert a == SetPart([
        [0, 1, 2, 3, 4, 5]
    ], domain_6)
    assert b == SetPart([
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)],
        [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)],
        [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)],
        [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3)]
    ], domain_6x4)
    assert c == SetPart([
        [ 0,  1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10, 11],
        [12, 13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22, 23]
    ], domain_24)

    ####################################################################################################################

    assert a.block_labels == {
        (0, 1, 2, 3, 4, 5): Boolf('0110 1001')
    }
    assert a.glove_compartment is None

    assert b.block_labels == {
        ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)): Boolf('0110 1001'),
        ((0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1)): Boolf('0110 1001', [0, 1, 3]),
        ((0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2)): Boolf('0110 1001', [0, 2, 3]),
        ((0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3)): Boolf('0110 1001', [1, 2, 3])
    }
    assert b.glove_compartment == [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]

    assert c.block_labels == {
        ( 0,  1,  2,  3,  4,  5): Boolf('0110 1001'),
        ( 6,  7,  8,  9, 10, 11): Boolf('0110 1001', [0, 1, 3]),
        (12, 13, 14, 15, 16, 17): Boolf('0110 1001', [0, 2, 3]),
        (18, 19, 20, 21, 22, 23): Boolf('0110 1001', [1, 2, 3])
    }
    assert c.glove_compartment is None
