from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf import Boolf
from discretehelpers.boolf.examples import miniri, medusa, barita, putuki, doguva, tomute, gepofu, vanatu, darimi

from .ex import AtomvalsMismatchError


def test_simple():
    only_1 = Boolf('01', [1])
    only_3 = Boolf('01', [3])
    conjunction = only_1 & only_3
    assert conjunction == Boolf('0001', [1, 3])
    assert conjunction.filtrated_boolf([1]) == only_1
    assert conjunction.filtrated_boolf([3]) == only_3


def test_raise():
    boolf = Boolf('0011 0101', [1, 3, 5])
    abbrev(AtomvalsMismatchError, [
        lambda: boolf.filtrated_boolf([1, 7]),
        lambda: boolf.filtrated_boolf([0, 1, 2]),
        lambda: boolf.filtrated_boolf([1, 3, 5, 7])
    ])


def test_medusa():
    assert medusa.filtrated_boolf([1, 2, 3]) == Boolf('1')  # BCD (A removed)
    assert medusa.filtrated_boolf([0, 1, 3]) == Boolf('1111 1110', [0, 1, 3])  # ABD (C removed)


def test_doguva():
    av = [0, 2, 3, 4, 5, 6, 7]  # ACDEFGH (B removed)
    assert doguva.filtrated_boolf(av) == Boolf(fullspots={0, 1, 2, 3, 4, 36, 6, 68, 100, 12, 14, 20, 52}, atomvals=av)

    av = [0, 1, 3, 4, 5, 6, 7]  # ABDEFGH (C removed)
    assert doguva.filtrated_boolf(av) == Boolf(fullspots={0, 1, 2, 3, 4, 6, 38, 70, 102, 12, 14, 22, 54}, atomvals=av)

    av = [0, 1, 3, 4, 5, 7]  # ABDEFH (CG removed)
    assert doguva.filtrated_boolf(av) == Boolf(fullspots={0, 1, 2, 3, 4, 6, 12, 14, 22, 38}, atomvals=av)

    av = [0, 2, 3, 6, 7]  # ACDGH (BEF removed)
    assert doguva.filtrated_boolf(av) == Boolf(fullspots={0, 1, 2, 3, 4, 6, 12, 20, 28}, atomvals=av)

    av = [0, 1, 2, 3, 6, 7]  # ABCDGH (EF removed)
    assert doguva.filtrated_boolf(av) == Boolf(fullspots={0, 1, 2, 3, 4, 5, 6, 58, 8, 10, 42, 12, 14, 26}, atomvals=av)

    av = [1, 2, 3, 4, 5, 7]  # BCDEFH (AG removed)
    assert doguva.filtrated_boolf(av) == Boolf(fullspots={0, 1, 2, 3, 4, 5, 6, 7, 37, 12, 14, 15, 21}, atomvals=av)


def test_tomute():
    av = [0, 1, 2, 3]  # ABCD (EFGH removed)
    assert tomute.filtrated_boolf(av) == vanatu

    av = [1, 2, 3, 4]  # BCDE (AFGH removed)
    assert tomute.filtrated_boolf(av) == darimi


def test_barita():
    av = [0, 1, 2]  # ABC (DEF removed)
    assert barita.filtrated_boolf(av) == Boolf('1')

    av = [0, 2, 3, 5]  # ACDF (BE removed)
    filtrate = barita.filtrated_boolf(av)
    assert filtrate == Boolf('1111 1010 1100 1000', [0, 2, 3, 5])
    frb = filtrate.root_boolf
    assert frb == putuki

    av = [1, 2, 3, 4, 5]  # BCDEF (A removed), D vanishes
    filtrate = barita.filtrated_boolf(av)
    assert filtrate == Boolf('1111 1000 1000 1000', [1, 2, 4, 5])
    frb = filtrate.root_boolf
    assert frb.vals(0, 3, 1, 2) == gepofu.root
    assert gepofu.vals(0, 2, 3, 1) == frb.root

    av = [0, 2, 3, 4, 5]  # ACDEF (B removed)
    filtrate = barita.filtrated_boolf(av)
    assert filtrate == Boolf(fullspots={0, 1, 2, 3, 4, 6, 8, 9, 12, 16, 17, 20, 24, 25, 28}, atomvals=av)
    frb = filtrate.root_boolf
    assert frb.vals(3, 4, 0, 1, 2) == miniri.root
    assert miniri.vals(2, 3, 4, 0, 1) == frb.root


def test_darimi():
    # The atomvals are [1, 2, 3, 4].
    assert darimi.filtrated_boolf([1, 2]) == Boolf('1')
    assert darimi.filtrated_boolf([2, 4]) == darimi.filtrated_boolf([1, 2, 4]) == Boolf('1101', [2, 4])
    assert darimi.filtrated_boolf([3, 4]) == Boolf('1101', [3, 4])
    assert darimi.filtrated_boolf([1, 2, 3]) == Boolf('1111 0111', [1, 2, 3])
    assert darimi.filtrated_boolf([1, 3, 4]) == Boolf('1101 0011', [1, 3, 4])
    assert darimi.filtrated_boolf([2, 3, 4]) == Boolf('1110 0001', [2, 3, 4])
