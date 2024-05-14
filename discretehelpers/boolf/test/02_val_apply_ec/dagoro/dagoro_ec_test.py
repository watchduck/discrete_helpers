from discretehelpers.boolf import Boolf

from discretehelpers.boolf.examples import dagoro


def test_family():
    family = dagoro.ec_family()
    assert dict(family.block_labels) == {
        (0,): Boolf('0101 1101 0010 0010'),
        (1,): Boolf('1010 1110 0001 0001'),
        (2,): Boolf('0101 0111 1000 1000'),
        (3,): Boolf('1010 1011 0100 0100'),
        (4,): Boolf('1101 0101 0010 0010'),
        (5,): Boolf('1110 1010 0001 0001'),
        (6,): Boolf('0111 0101 1000 1000'),
        (7,): Boolf('1011 1010 0100 0100'),
        (8,): Boolf('0010 0010 0101 1101'),
        (9,): Boolf('0001 0001 1010 1110'),
        (10,): Boolf('1000 1000 0101 0111'),
        (11,): Boolf('0100 0100 1010 1011'),
        (12,): Boolf('0010 0010 1101 0101'),
        (13,): Boolf('0001 0001 1110 1010'),
        (14,): Boolf('1000 1000 0111 0101'),
        (15,): Boolf('0100 0100 1011 1010')
    }


def test_clan():
    clan = dagoro.ec_clan()
    assert dict(clan.block_labels) == {
        ((0, 0),): Boolf('0101 1101 0010 0010'),
        ((0, 1),): Boolf('0011 1011 0100 0100'),
        ((0, 2),): Boolf('0111 0101 0000 1010'),
        ((0, 3),): Boolf('0010 1111 0101 0000'),
        ((0, 4),): Boolf('0111 0011 0000 1100'),
        ((0, 5),): Boolf('0100 1111 0011 0000'),
        ((0, 6),): Boolf('0101 0010 1101 0010'),
        ((0, 7),): Boolf('0011 0100 1011 0100'),
        ((0, 8),): Boolf('0111 0000 0101 1010'),
        ((0, 9),): Boolf('0010 0101 1111 0000'),
        ((0, 10),): Boolf('0111 0000 0011 1100'),
        ((0, 11),): Boolf('0100 0011 1111 0000'),
        ((0, 12),): Boolf('0100 0110 1100 0110'),
        ((0, 13),): Boolf('0001 1100 1001 1100'),
        ((0, 14),): Boolf('0100 1100 0110 0110'),
        ((0, 15),): Boolf('0001 1001 1100 1100'),
        ((0, 16),): Boolf('0100 1100 0011 1100'),
        ((0, 17),): Boolf('0100 0011 1100 1100'),
        ((0, 18),): Boolf('0010 0110 1010 0110'),
        ((0, 19),): Boolf('0001 1010 1001 1010'),
        ((0, 20),): Boolf('0010 1010 0110 0110'),
        ((0, 21),): Boolf('0001 1001 1010 1010'),
        ((0, 22),): Boolf('0010 1010 0101 1010'),
        ((0, 23),): Boolf('0010 0101 1010 1010'),
        ((1, 0),): Boolf('1010 1110 0001 0001'),
        ((1, 1),): Boolf('0011 0111 1000 1000'),
        ((1, 2),): Boolf('1011 1010 0000 0101'),
        ((1, 3),): Boolf('0001 1111 1010 0000'),
        ((1, 4),): Boolf('1011 0011 0000 1100'),
        ((1, 5),): Boolf('1000 1111 0011 0000'),
        ((1, 6),): Boolf('1010 0001 1110 0001'),
        ((1, 7),): Boolf('0011 1000 0111 1000'),
        ((1, 8),): Boolf('1011 0000 1010 0101'),
        ((1, 9),): Boolf('0001 1010 1111 0000'),
        ((1, 10),): Boolf('1011 0000 0011 1100'),
        ((1, 11),): Boolf('1000 0011 1111 0000'),
        ((1, 12),): Boolf('1000 1001 1100 1001'),
        ((1, 13),): Boolf('0010 1100 0110 1100'),
        ((1, 14),): Boolf('1000 1100 1001 1001'),
        ((1, 15),): Boolf('0010 0110 1100 1100'),
        ((1, 16),): Boolf('1000 1100 0011 1100'),
        ((1, 17),): Boolf('1000 0011 1100 1100'),
        ((1, 18),): Boolf('0001 1001 0101 1001'),
        ((1, 19),): Boolf('0010 0101 0110 0101'),
        ((1, 20),): Boolf('0001 0101 1001 1001'),
        ((1, 21),): Boolf('0010 0110 0101 0101'),
        ((1, 22),): Boolf('0001 0101 1010 0101'),
        ((1, 23),): Boolf('0001 1010 0101 0101'),
        ((2, 0),): Boolf('0101 0111 1000 1000'),
        ((2, 1),): Boolf('1100 1110 0001 0001'),
        ((2, 2),): Boolf('1101 0101 0000 1010'),
        ((2, 3),): Boolf('1000 1111 0101 0000'),
        ((2, 4),): Boolf('1101 1100 0000 0011'),
        ((2, 5),): Boolf('0001 1111 1100 0000'),
        ((2, 6),): Boolf('0101 1000 0111 1000'),
        ((2, 7),): Boolf('1100 0001 1110 0001'),
        ((2, 8),): Boolf('1101 0000 0101 1010'),
        ((2, 9),): Boolf('1000 0101 1111 0000'),
        ((2, 10),): Boolf('1101 0000 1100 0011'),
        ((2, 11),): Boolf('0001 1100 1111 0000'),
        ((2, 12),): Boolf('0001 1001 0011 1001'),
        ((2, 13),): Boolf('0100 0011 0110 0011'),
        ((2, 14),): Boolf('0001 0011 1001 1001'),
        ((2, 15),): Boolf('0100 0110 0011 0011'),
        ((2, 16),): Boolf('0001 0011 1100 0011'),
        ((2, 17),): Boolf('0001 1100 0011 0011'),
        ((2, 18),): Boolf('1000 1001 1010 1001'),
        ((2, 19),): Boolf('0100 1010 0110 1010'),
        ((2, 20),): Boolf('1000 1010 1001 1001'),
        ((2, 21),): Boolf('0100 0110 1010 1010'),
        ((2, 22),): Boolf('1000 1010 0101 1010'),
        ((2, 23),): Boolf('1000 0101 1010 1010'),
        ((3, 0),): Boolf('1010 1011 0100 0100'),
        ((3, 1),): Boolf('1100 1101 0010 0010'),
        ((3, 2),): Boolf('1110 1010 0000 0101'),
        ((3, 3),): Boolf('0100 1111 1010 0000'),
        ((3, 4),): Boolf('1110 1100 0000 0011'),
        ((3, 5),): Boolf('0010 1111 1100 0000'),
        ((3, 6),): Boolf('1010 0100 1011 0100'),
        ((3, 7),): Boolf('1100 0010 1101 0010'),
        ((3, 8),): Boolf('1110 0000 1010 0101'),
        ((3, 9),): Boolf('0100 1010 1111 0000'),
        ((3, 10),): Boolf('1110 0000 1100 0011'),
        ((3, 11),): Boolf('0010 1100 1111 0000'),
        ((3, 12),): Boolf('0010 0110 0011 0110'),
        ((3, 13),): Boolf('1000 0011 1001 0011'),
        ((3, 14),): Boolf('0010 0011 0110 0110'),
        ((3, 15),): Boolf('1000 1001 0011 0011'),
        ((3, 16),): Boolf('0010 0011 1100 0011'),
        ((3, 17),): Boolf('0010 1100 0011 0011'),
        ((3, 18),): Boolf('0100 0110 0101 0110'),
        ((3, 19),): Boolf('1000 0101 1001 0101'),
        ((3, 20),): Boolf('0100 0101 0110 0110'),
        ((3, 21),): Boolf('1000 1001 0101 0101'),
        ((3, 22),): Boolf('0100 0101 1010 0101'),
        ((3, 23),): Boolf('0100 1010 0101 0101'),
        ((4, 0),): Boolf('1101 0101 0010 0010'),
        ((4, 1),): Boolf('1011 0011 0100 0100'),
        ((4, 2),): Boolf('0101 0111 1010 0000'),
        ((4, 3),): Boolf('1111 0010 0000 0101'),
        ((4, 4),): Boolf('0011 0111 1100 0000'),
        ((4, 5),): Boolf('1111 0100 0000 0011'),
        ((4, 6),): Boolf('0010 0101 0010 1101'),
        ((4, 7),): Boolf('0100 0011 0100 1011'),
        ((4, 8),): Boolf('0000 0111 1010 0101'),
        ((4, 9),): Boolf('0101 0010 0000 1111'),
        ((4, 10),): Boolf('0000 0111 1100 0011'),
        ((4, 11),): Boolf('0011 0100 0000 1111'),
        ((4, 12),): Boolf('0110 0100 0110 1100'),
        ((4, 13),): Boolf('1100 0001 1100 1001'),
        ((4, 14),): Boolf('1100 0100 0110 0110'),
        ((4, 15),): Boolf('1001 0001 1100 1100'),
        ((4, 16),): Boolf('1100 0100 1100 0011'),
        ((4, 17),): Boolf('0011 0100 1100 1100'),
        ((4, 18),): Boolf('0110 0010 0110 1010'),
        ((4, 19),): Boolf('1010 0001 1010 1001'),
        ((4, 20),): Boolf('1010 0010 0110 0110'),
        ((4, 21),): Boolf('1001 0001 1010 1010'),
        ((4, 22),): Boolf('1010 0010 1010 0101'),
        ((4, 23),): Boolf('0101 0010 1010 1010'),
        ((5, 0),): Boolf('1110 1010 0001 0001'),
        ((5, 1),): Boolf('0111 0011 1000 1000'),
        ((5, 2),): Boolf('1010 1011 0101 0000'),
        ((5, 3),): Boolf('1111 0001 0000 1010'),
        ((5, 4),): Boolf('0011 1011 1100 0000'),
        ((5, 5),): Boolf('1111 1000 0000 0011'),
        ((5, 6),): Boolf('0001 1010 0001 1110'),
        ((5, 7),): Boolf('1000 0011 1000 0111'),
        ((5, 8),): Boolf('0000 1011 0101 1010'),
        ((5, 9),): Boolf('1010 0001 0000 1111'),
        ((5, 10),): Boolf('0000 1011 1100 0011'),
        ((5, 11),): Boolf('0011 1000 0000 1111'),
        ((5, 12),): Boolf('1001 1000 1001 1100'),
        ((5, 13),): Boolf('1100 0010 1100 0110'),
        ((5, 14),): Boolf('1100 1000 1001 1001'),
        ((5, 15),): Boolf('0110 0010 1100 1100'),
        ((5, 16),): Boolf('1100 1000 1100 0011'),
        ((5, 17),): Boolf('0011 1000 1100 1100'),
        ((5, 18),): Boolf('1001 0001 1001 0101'),
        ((5, 19),): Boolf('0101 0010 0101 0110'),
        ((5, 20),): Boolf('0101 0001 1001 1001'),
        ((5, 21),): Boolf('0110 0010 0101 0101'),
        ((5, 22),): Boolf('0101 0001 0101 1010'),
        ((5, 23),): Boolf('1010 0001 0101 0101'),
        ((6, 0),): Boolf('0111 0101 1000 1000'),
        ((6, 1),): Boolf('1110 1100 0001 0001'),
        ((6, 2),): Boolf('0101 1101 1010 0000'),
        ((6, 3),): Boolf('1111 1000 0000 0101'),
        ((6, 4),): Boolf('1100 1101 0011 0000'),
        ((6, 5),): Boolf('1111 0001 0000 1100'),
        ((6, 6),): Boolf('1000 0101 1000 0111'),
        ((6, 7),): Boolf('0001 1100 0001 1110'),
        ((6, 8),): Boolf('0000 1101 1010 0101'),
        ((6, 9),): Boolf('0101 1000 0000 1111'),
        ((6, 10),): Boolf('0000 1101 0011 1100'),
        ((6, 11),): Boolf('1100 0001 0000 1111'),
        ((6, 12),): Boolf('1001 0001 1001 0011'),
        ((6, 13),): Boolf('0011 0100 0011 0110'),
        ((6, 14),): Boolf('0011 0001 1001 1001'),
        ((6, 15),): Boolf('0110 0100 0011 0011'),
        ((6, 16),): Boolf('0011 0001 0011 1100'),
        ((6, 17),): Boolf('1100 0001 0011 0011'),
        ((6, 18),): Boolf('1001 1000 1001 1010'),
        ((6, 19),): Boolf('1010 0100 1010 0110'),
        ((6, 20),): Boolf('1010 1000 1001 1001'),
        ((6, 21),): Boolf('0110 0100 1010 1010'),
        ((6, 22),): Boolf('1010 1000 1010 0101'),
        ((6, 23),): Boolf('0101 1000 1010 1010'),
        ((7, 0),): Boolf('1011 1010 0100 0100'),
        ((7, 1),): Boolf('1101 1100 0010 0010'),
        ((7, 2),): Boolf('1010 1110 0101 0000'),
        ((7, 3),): Boolf('1111 0100 0000 1010'),
        ((7, 4),): Boolf('1100 1110 0011 0000'),
        ((7, 5),): Boolf('1111 0010 0000 1100'),
        ((7, 6),): Boolf('0100 1010 0100 1011'),
        ((7, 7),): Boolf('0010 1100 0010 1101'),
        ((7, 8),): Boolf('0000 1110 0101 1010'),
        ((7, 9),): Boolf('1010 0100 0000 1111'),
        ((7, 10),): Boolf('0000 1110 0011 1100'),
        ((7, 11),): Boolf('1100 0010 0000 1111'),
        ((7, 12),): Boolf('0110 0010 0110 0011'),
        ((7, 13),): Boolf('0011 1000 0011 1001'),
        ((7, 14),): Boolf('0011 0010 0110 0110'),
        ((7, 15),): Boolf('1001 1000 0011 0011'),
        ((7, 16),): Boolf('0011 0010 0011 1100'),
        ((7, 17),): Boolf('1100 0010 0011 0011'),
        ((7, 18),): Boolf('0110 0100 0110 0101'),
        ((7, 19),): Boolf('0101 1000 0101 1001'),
        ((7, 20),): Boolf('0101 0100 0110 0110'),
        ((7, 21),): Boolf('1001 1000 0101 0101'),
        ((7, 22),): Boolf('0101 0100 0101 1010'),
        ((7, 23),): Boolf('1010 0100 0101 0101'),
        ((8, 0),): Boolf('0010 0010 0101 1101'),
        ((8, 1),): Boolf('0100 0100 0011 1011'),
        ((8, 2),): Boolf('0000 1010 0111 0101'),
        ((8, 3),): Boolf('0101 0000 0010 1111'),
        ((8, 4),): Boolf('0000 1100 0111 0011'),
        ((8, 5),): Boolf('0011 0000 0100 1111'),
        ((8, 6),): Boolf('1101 0010 0101 0010'),
        ((8, 7),): Boolf('1011 0100 0011 0100'),
        ((8, 8),): Boolf('0101 1010 0111 0000'),
        ((8, 9),): Boolf('1111 0000 0010 0101'),
        ((8, 10),): Boolf('0011 1100 0111 0000'),
        ((8, 11),): Boolf('1111 0000 0100 0011'),
        ((8, 12),): Boolf('1100 0110 0100 0110'),
        ((8, 13),): Boolf('1001 1100 0001 1100'),
        ((8, 14),): Boolf('0110 0110 0100 1100'),
        ((8, 15),): Boolf('1100 1100 0001 1001'),
        ((8, 16),): Boolf('0011 1100 0100 1100'),
        ((8, 17),): Boolf('1100 1100 0100 0011'),
        ((8, 18),): Boolf('1010 0110 0010 0110'),
        ((8, 19),): Boolf('1001 1010 0001 1010'),
        ((8, 20),): Boolf('0110 0110 0010 1010'),
        ((8, 21),): Boolf('1010 1010 0001 1001'),
        ((8, 22),): Boolf('0101 1010 0010 1010'),
        ((8, 23),): Boolf('1010 1010 0010 0101'),
        ((9, 0),): Boolf('0001 0001 1010 1110'),
        ((9, 1),): Boolf('1000 1000 0011 0111'),
        ((9, 2),): Boolf('0000 0101 1011 1010'),
        ((9, 3),): Boolf('1010 0000 0001 1111'),
        ((9, 4),): Boolf('0000 1100 1011 0011'),
        ((9, 5),): Boolf('0011 0000 1000 1111'),
        ((9, 6),): Boolf('1110 0001 1010 0001'),
        ((9, 7),): Boolf('0111 1000 0011 1000'),
        ((9, 8),): Boolf('1010 0101 1011 0000'),
        ((9, 9),): Boolf('1111 0000 0001 1010'),
        ((9, 10),): Boolf('0011 1100 1011 0000'),
        ((9, 11),): Boolf('1111 0000 1000 0011'),
        ((9, 12),): Boolf('1100 1001 1000 1001'),
        ((9, 13),): Boolf('0110 1100 0010 1100'),
        ((9, 14),): Boolf('1001 1001 1000 1100'),
        ((9, 15),): Boolf('1100 1100 0010 0110'),
        ((9, 16),): Boolf('0011 1100 1000 1100'),
        ((9, 17),): Boolf('1100 1100 1000 0011'),
        ((9, 18),): Boolf('0101 1001 0001 1001'),
        ((9, 19),): Boolf('0110 0101 0010 0101'),
        ((9, 20),): Boolf('1001 1001 0001 0101'),
        ((9, 21),): Boolf('0101 0101 0010 0110'),
        ((9, 22),): Boolf('1010 0101 0001 0101'),
        ((9, 23),): Boolf('0101 0101 0001 1010'),
        ((10, 0),): Boolf('1000 1000 0101 0111'),
        ((10, 1),): Boolf('0001 0001 1100 1110'),
        ((10, 2),): Boolf('0000 1010 1101 0101'),
        ((10, 3),): Boolf('0101 0000 1000 1111'),
        ((10, 4),): Boolf('0000 0011 1101 1100'),
        ((10, 5),): Boolf('1100 0000 0001 1111'),
        ((10, 6),): Boolf('0111 1000 0101 1000'),
        ((10, 7),): Boolf('1110 0001 1100 0001'),
        ((10, 8),): Boolf('0101 1010 1101 0000'),
        ((10, 9),): Boolf('1111 0000 1000 0101'),
        ((10, 10),): Boolf('1100 0011 1101 0000'),
        ((10, 11),): Boolf('1111 0000 0001 1100'),
        ((10, 12),): Boolf('0011 1001 0001 1001'),
        ((10, 13),): Boolf('0110 0011 0100 0011'),
        ((10, 14),): Boolf('1001 1001 0001 0011'),
        ((10, 15),): Boolf('0011 0011 0100 0110'),
        ((10, 16),): Boolf('1100 0011 0001 0011'),
        ((10, 17),): Boolf('0011 0011 0001 1100'),
        ((10, 18),): Boolf('1010 1001 1000 1001'),
        ((10, 19),): Boolf('0110 1010 0100 1010'),
        ((10, 20),): Boolf('1001 1001 1000 1010'),
        ((10, 21),): Boolf('1010 1010 0100 0110'),
        ((10, 22),): Boolf('0101 1010 1000 1010'),
        ((10, 23),): Boolf('1010 1010 1000 0101'),
        ((11, 0),): Boolf('0100 0100 1010 1011'),
        ((11, 1),): Boolf('0010 0010 1100 1101'),
        ((11, 2),): Boolf('0000 0101 1110 1010'),
        ((11, 3),): Boolf('1010 0000 0100 1111'),
        ((11, 4),): Boolf('0000 0011 1110 1100'),
        ((11, 5),): Boolf('1100 0000 0010 1111'),
        ((11, 6),): Boolf('1011 0100 1010 0100'),
        ((11, 7),): Boolf('1101 0010 1100 0010'),
        ((11, 8),): Boolf('1010 0101 1110 0000'),
        ((11, 9),): Boolf('1111 0000 0100 1010'),
        ((11, 10),): Boolf('1100 0011 1110 0000'),
        ((11, 11),): Boolf('1111 0000 0010 1100'),
        ((11, 12),): Boolf('0011 0110 0010 0110'),
        ((11, 13),): Boolf('1001 0011 1000 0011'),
        ((11, 14),): Boolf('0110 0110 0010 0011'),
        ((11, 15),): Boolf('0011 0011 1000 1001'),
        ((11, 16),): Boolf('1100 0011 0010 0011'),
        ((11, 17),): Boolf('0011 0011 0010 1100'),
        ((11, 18),): Boolf('0101 0110 0100 0110'),
        ((11, 19),): Boolf('1001 0101 1000 0101'),
        ((11, 20),): Boolf('0110 0110 0100 0101'),
        ((11, 21),): Boolf('0101 0101 1000 1001'),
        ((11, 22),): Boolf('1010 0101 0100 0101'),
        ((11, 23),): Boolf('0101 0101 0100 1010'),
        ((12, 0),): Boolf('0010 0010 1101 0101'),
        ((12, 1),): Boolf('0100 0100 1011 0011'),
        ((12, 2),): Boolf('1010 0000 0101 0111'),
        ((12, 3),): Boolf('0000 0101 1111 0010'),
        ((12, 4),): Boolf('1100 0000 0011 0111'),
        ((12, 5),): Boolf('0000 0011 1111 0100'),
        ((12, 6),): Boolf('0010 1101 0010 0101'),
        ((12, 7),): Boolf('0100 1011 0100 0011'),
        ((12, 8),): Boolf('1010 0101 0000 0111'),
        ((12, 9),): Boolf('0000 1111 0101 0010'),
        ((12, 10),): Boolf('1100 0011 0000 0111'),
        ((12, 11),): Boolf('0000 1111 0011 0100'),
        ((12, 12),): Boolf('0110 1100 0110 0100'),
        ((12, 13),): Boolf('1100 1001 1100 0001'),
        ((12, 14),): Boolf('0110 0110 1100 0100'),
        ((12, 15),): Boolf('1100 1100 1001 0001'),
        ((12, 16),): Boolf('1100 0011 1100 0100'),
        ((12, 17),): Boolf('1100 1100 0011 0100'),
        ((12, 18),): Boolf('0110 1010 0110 0010'),
        ((12, 19),): Boolf('1010 1001 1010 0001'),
        ((12, 20),): Boolf('0110 0110 1010 0010'),
        ((12, 21),): Boolf('1010 1010 1001 0001'),
        ((12, 22),): Boolf('1010 0101 1010 0010'),
        ((12, 23),): Boolf('1010 1010 0101 0010'),
        ((13, 0),): Boolf('0001 0001 1110 1010'),
        ((13, 1),): Boolf('1000 1000 0111 0011'),
        ((13, 2),): Boolf('0101 0000 1010 1011'),
        ((13, 3),): Boolf('0000 1010 1111 0001'),
        ((13, 4),): Boolf('1100 0000 0011 1011'),
        ((13, 5),): Boolf('0000 0011 1111 1000'),
        ((13, 6),): Boolf('0001 1110 0001 1010'),
        ((13, 7),): Boolf('1000 0111 1000 0011'),
        ((13, 8),): Boolf('0101 1010 0000 1011'),
        ((13, 9),): Boolf('0000 1111 1010 0001'),
        ((13, 10),): Boolf('1100 0011 0000 1011'),
        ((13, 11),): Boolf('0000 1111 0011 1000'),
        ((13, 12),): Boolf('1001 1100 1001 1000'),
        ((13, 13),): Boolf('1100 0110 1100 0010'),
        ((13, 14),): Boolf('1001 1001 1100 1000'),
        ((13, 15),): Boolf('1100 1100 0110 0010'),
        ((13, 16),): Boolf('1100 0011 1100 1000'),
        ((13, 17),): Boolf('1100 1100 0011 1000'),
        ((13, 18),): Boolf('1001 0101 1001 0001'),
        ((13, 19),): Boolf('0101 0110 0101 0010'),
        ((13, 20),): Boolf('1001 1001 0101 0001'),
        ((13, 21),): Boolf('0101 0101 0110 0010'),
        ((13, 22),): Boolf('0101 1010 0101 0001'),
        ((13, 23),): Boolf('0101 0101 1010 0001'),
        ((14, 0),): Boolf('1000 1000 0111 0101'),
        ((14, 1),): Boolf('0001 0001 1110 1100'),
        ((14, 2),): Boolf('1010 0000 0101 1101'),
        ((14, 3),): Boolf('0000 0101 1111 1000'),
        ((14, 4),): Boolf('0011 0000 1100 1101'),
        ((14, 5),): Boolf('0000 1100 1111 0001'),
        ((14, 6),): Boolf('1000 0111 1000 0101'),
        ((14, 7),): Boolf('0001 1110 0001 1100'),
        ((14, 8),): Boolf('1010 0101 0000 1101'),
        ((14, 9),): Boolf('0000 1111 0101 1000'),
        ((14, 10),): Boolf('0011 1100 0000 1101'),
        ((14, 11),): Boolf('0000 1111 1100 0001'),
        ((14, 12),): Boolf('1001 0011 1001 0001'),
        ((14, 13),): Boolf('0011 0110 0011 0100'),
        ((14, 14),): Boolf('1001 1001 0011 0001'),
        ((14, 15),): Boolf('0011 0011 0110 0100'),
        ((14, 16),): Boolf('0011 1100 0011 0001'),
        ((14, 17),): Boolf('0011 0011 1100 0001'),
        ((14, 18),): Boolf('1001 1010 1001 1000'),
        ((14, 19),): Boolf('1010 0110 1010 0100'),
        ((14, 20),): Boolf('1001 1001 1010 1000'),
        ((14, 21),): Boolf('1010 1010 0110 0100'),
        ((14, 22),): Boolf('1010 0101 1010 1000'),
        ((14, 23),): Boolf('1010 1010 0101 1000'),
        ((15, 0),): Boolf('0100 0100 1011 1010'),
        ((15, 1),): Boolf('0010 0010 1101 1100'),
        ((15, 2),): Boolf('0101 0000 1010 1110'),
        ((15, 3),): Boolf('0000 1010 1111 0100'),
        ((15, 4),): Boolf('0011 0000 1100 1110'),
        ((15, 5),): Boolf('0000 1100 1111 0010'),
        ((15, 6),): Boolf('0100 1011 0100 1010'),
        ((15, 7),): Boolf('0010 1101 0010 1100'),
        ((15, 8),): Boolf('0101 1010 0000 1110'),
        ((15, 9),): Boolf('0000 1111 1010 0100'),
        ((15, 10),): Boolf('0011 1100 0000 1110'),
        ((15, 11),): Boolf('0000 1111 1100 0010'),
        ((15, 12),): Boolf('0110 0011 0110 0010'),
        ((15, 13),): Boolf('0011 1001 0011 1000'),
        ((15, 14),): Boolf('0110 0110 0011 0010'),
        ((15, 15),): Boolf('0011 0011 1001 1000'),
        ((15, 16),): Boolf('0011 1100 0011 0010'),
        ((15, 17),): Boolf('0011 0011 1100 0010'),
        ((15, 18),): Boolf('0110 0101 0110 0100'),
        ((15, 19),): Boolf('0101 1001 0101 1000'),
        ((15, 20),): Boolf('0110 0110 0101 0100'),
        ((15, 21),): Boolf('0101 0101 1001 1000'),
        ((15, 22),): Boolf('0101 1010 0101 0100'),
        ((15, 23),): Boolf('0101 0101 1010 0100')
    }