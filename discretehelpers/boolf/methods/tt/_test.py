from discretehelpers.boolf import Boolf
from discretehelpers.binv import Binv

from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.ex import ArgMismatchError, ArgTooSmallError

from discretehelpers.boolf.examples import tokosi


def test():
    seq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    boolf = Boolf(seq)
    assert boolf.tt(5) == boolf.tt([0, 1, 2, 3, 4]) == Binv(seq * 2)
    assert boolf.tt() == boolf.tt(4) == boolf.tt([0, 1, 2, 3]) == Binv(seq)
    assert boolf.tt({1, 2, 3}) == Binv('0000 0011')
    assert boolf.tt({2, 3}) == Binv('0001')

    abbrev(ArgTooSmallError, [
        lambda: boolf.tt(3)
    ])
    abbrev(ArgMismatchError, [
        lambda: boolf.tt({3}),
        lambda: boolf.tt({1, 3})
    ])


def test_b1():
    assert tokosi.tt([1, 3, 5, 7, 9]) == tokosi.dense_tt == Binv('00010010000000000000000010001100')
    assert tokosi.tt() == tokosi.tt(10) == tokosi.tt(list(range(10))) == Binv(length=1024, exposet={10, 11, 14, 15, 26, 27, 30, 31, 40, 41, 44, 45, 56, 57, 60, 61, 74, 75, 78, 79, 90, 91, 94, 95, 104, 105, 108, 109, 120, 121, 124, 125, 640, 641, 644, 645, 656, 657, 660, 661, 672, 673, 674, 675, 676, 677, 678, 679, 688, 689, 690, 691, 692, 693, 694, 695, 704, 705, 708, 709, 720, 721, 724, 725, 736, 737, 738, 739, 740, 741, 742, 743, 752, 753, 754, 755, 756, 757, 758, 759, 266, 267, 270, 271, 282, 283, 286, 287, 296, 297, 300, 301, 312, 313, 316, 317, 330, 331, 334, 335, 346, 347, 350, 351, 360, 361, 364, 365, 376, 377, 380, 381, 896, 897, 900, 901, 912, 913, 916, 917, 928, 929, 930, 931, 932, 933, 934, 935, 944, 945, 946, 947, 948, 949, 950, 951, 960, 961, 964, 965, 976, 977, 980, 981, 992, 993, 994, 995, 996, 997, 998, 999, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015})
    assert tokosi.tt([1, 3, 5, 7, 9, 11]) == Binv('0001001000000000000000001000110000010010000000000000000010001100')
    assert tokosi.tt([0, 1, 3, 5, 7, 9]) == Binv('0000001100001100000000000000000000000000000000001100000011110000')

    abbrev(ArgTooSmallError, [
        lambda: tokosi.tt(9)
    ])
    abbrev(ArgMismatchError, [
        lambda: tokosi.tt([1, 3, 5, 9]),
        lambda: tokosi.tt([1, 3, 5, 7])
    ])
