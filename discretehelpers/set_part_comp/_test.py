from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.set_part import SetPart

from . import SetPartComp
from .ex import *


def test_1():
    spc = SetPartComp()
    spc.set_equal(2, 3)
    spc.set_equal(3, 4)
    spc.set_equal(5, 6)
    spc.set_equal(7, 8)
    spc.set_comp(8, 3)
    assert spc.equal_part.blocks == [[2, 3, 4], [5, 6], [7, 8]]
    assert spc.comp_pairs == {(2, 7)}

    abbrev(SetEqualComplementsError, [
        lambda: spc.set_equal(2, 7),
        lambda: spc.set_equal(8, 4)
    ])
    abbrev(SetCompEqualsError, [
        lambda: spc.set_comp(2, 4),
        lambda: spc.set_comp(5, 6),
        lambda: spc.set_comp(8, 7)
    ])

    spc.set_equal(5, 1)
    assert spc.equal_part.blocks == [[1, 5, 6], [2, 3, 4], [7, 8]]
    assert spc.comp_pairs == {(2, 7)}

    spc.set_equal(0, 8)
    assert spc.equal_part.blocks == [[0, 7, 8], [1, 5, 6], [2, 3, 4]]
    assert spc.comp_pairs == {(0, 2)}

    assert spc.are_comp(0, 4)
    assert spc.are_comp(3, 7)
    assert not spc.are_comp(5, 3)
    assert not spc.are_comp(7, 8)
    assert not spc.are_comp(0, 99)
    assert not spc.are_comp(88, 99)

    assert spc.are_equal(1, 6)
    assert not spc.are_equal(5, 7)
    assert not spc.are_equal(5, 99)
    assert not spc.are_equal(88, 99)

    spc.set_comp(8, 9)
    assert spc.equal_part.blocks == [[0, 7, 8], [1, 5, 6], [2, 3, 4, 9]]
    assert spc.comp_pairs == {(0, 2)}


def test_2():
    part = [[0, 1], [2, 3], [4, 5], [6, 7]]
    comp = {(0, 2), (4, 6)}
    spc = SetPartComp(part, comp)
    assert spc.equal_part == SetPart(part, 'Z')
    assert spc.comp_pairs == comp

    abbrev(SetEqualComplementsError, [
        lambda: spc.set_equal(1, 3)
    ])
    abbrev(SetCompEqualsError, [
        lambda: spc.set_comp(0, 1)
    ])

    spc.set_comp(3, 4)
    assert spc.equal_part == SetPart([[0, 1, 4, 5], [2, 3, 6, 7]], 'Z')
    assert spc.comp_pairs == {(0, 2)}


def test_raise():
    abbrev(CompWithoutPartError, [
        lambda: SetPartComp(None, {(1, 2)}),
        lambda: SetPartComp(comp_pairs=set())
    ])
    abbrev(PartCompMismatchError, [
        lambda: SetPartComp([[1, 2]], {(1, 2)}),
        lambda: SetPartComp([[1, 2, 3], [4, 5]], {(1, 3)})
    ])


def test_no_comp():
    part = [[0, 1], [2, 3], [4, 5], [6, 7]]

    spc = SetPartComp(part)
    spc.set_equal(0, 3)
    assert spc.equal_part == SetPart([[0, 1, 2, 3], [4, 5], [6, 7]], 'Z')
    assert spc.comp_pairs == set()

    spc = SetPartComp(part)
    spc.set_comp(0, 3)
    assert spc.equal_part == SetPart([[0, 1], [2, 3], [4, 5], [6, 7]], 'Z')
    assert spc.comp_pairs == {(0, 2)}


def test_one_comp():
    part = [[0, 1], [2, 3], [4, 5], [6, 7]]
    comp = {(2, 4)}

    spc = SetPartComp(part, comp)
    spc.set_equal(1, 3)
    assert spc.equal_part == SetPart([[0, 1, 2, 3], [4, 5], [6, 7]], 'Z')
    assert spc.comp_pairs == {(0, 4)}

    spc = SetPartComp(part, comp)
    spc.set_comp(0, 3)
    assert spc.equal_part == SetPart([[0, 1, 4, 5], [2, 3], [6, 7]], 'Z')
    assert spc.comp_pairs == {(0, 2)}
    assert spc.related_part() == SetPart([[0, 1, 4, 5, 2, 3], [6, 7]], 'Z')


def test_both_comp():
    part = [[0, 1], [2, 3], [4, 5], [6, 7]]
    comp = {(0, 6), (2, 4)}

    spc = SetPartComp(part, comp)
    spc.set_equal(1, 3)
    assert spc.equal_part == SetPart([[0, 1, 2, 3], [4, 5, 6, 7]], 'Z')
    assert spc.comp_pairs == {(0, 4)}

    spc = SetPartComp(part, comp)
    spc.set_comp(1, 3)
    assert spc.equal_part == SetPart([[0, 1, 4, 5], [2, 3, 6, 7]], 'Z')
    assert spc.comp_pairs == {(0, 2)}
    assert spc.related_part() == SetPart([[0, 1, 4, 5, 2, 3, 6, 7]], 'Z')


def test_with_image():  # see README
    spc = SetPartComp([[3, 4], [5, 6, 7], [8, 9], [20, 30]], {(1, 2), (3, 8), (10, 11)})
    assert spc.related_part().blocks == [[1, 2], [3, 4, 8, 9], [5, 6, 7], [10, 11], [20, 30]]
    assert spc.get_block(4) == [3, 4]
    assert spc.get_repr(4) == 3

    spc.set_equal(2, 4)
    assert spc == SetPartComp([[1, 8, 9], [2, 3, 4], [5, 6, 7], [20, 30]], {(1, 2), (10, 11)})
    assert spc.related_part().blocks == [[1, 2, 3, 4, 8, 9], [5, 6, 7], [10, 11], [20, 30]]
    assert spc.number_of_related_blocks() == 4
    assert spc.length() == 31

    spc.set_comp(11, 20)
    assert spc == SetPartComp([[1, 8, 9], [2, 3, 4], [5, 6, 7], [10, 20, 30]], {(1, 2), (10, 11)})
    assert spc.get_block(20) == [10, 20, 30]
    assert spc.get_repr(20) == 10

    spc.set_comp(12, 30)
    assert spc == SetPartComp([[1, 8, 9], [2, 3, 4], [5, 6, 7], [10, 20, 30], [11, 12]], {(1, 2), (10, 11)})

    spc.set_equal(6, 13)
    assert spc == SetPartComp([[1, 8, 9], [2, 3, 4], [5, 6, 7, 13], [10, 20, 30], [11, 12]], {(1, 2), (10, 11)})

    spc.set_comp(3, 30)
    assert spc == SetPartComp([[1, 8, 9, 10, 20, 30], [2, 3, 4, 11, 12], [5, 6, 7, 13]], {(1, 2)})
    assert spc.related_part().blocks == [[1, 2, 3, 4, 8, 9, 10, 11, 12, 20, 30], [5, 6, 7, 13]]

    spc.set_comp(40, 50)
    assert spc == SetPartComp([[1, 8, 9, 10, 20, 30], [2, 3, 4, 11, 12], [5, 6, 7, 13]], {(1, 2), (40, 50)})
    assert spc.related_part().blocks == [[1, 2, 3, 4, 8, 9, 10, 11, 12, 20, 30], [5, 6, 7, 13], [40, 50]]
    assert spc.number_of_related_blocks() == 3
    assert spc.length() == 51
    assert spc.affected_elements() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20, 30, 40, 50]
    assert spc.number_of_affected_elements() == 17

    spc.set_equal(60, 70)
    assert spc == SetPartComp([[1, 8, 9, 10, 20, 30], [2, 3, 4, 11, 12], [5, 6, 7, 13], [60, 70]], {(1, 2), (40, 50)})
    assert spc.get_block(4) == [2, 3, 4, 11, 12]
    assert spc.get_repr(4) == 2

    spc.set_comp(0, 70)
    assert spc == SetPartComp([[1, 8, 9, 10, 20, 30], [2, 3, 4, 11, 12], [5, 6, 7, 13], [60, 70]], {(1, 2), (40, 50), (0, 60)})
    assert spc.related_part().blocks == [[0, 60, 70], [1, 2, 3, 4, 8, 9, 10, 11, 12, 20, 30], [5, 6, 7, 13], [40, 50]]
    assert spc.number_of_related_blocks() == 4
    assert spc.length() == 71

    spc.set_comp(0, 40)
    assert spc == SetPartComp([[0, 50], [1, 8, 9, 10, 20, 30], [2, 3, 4, 11, 12], [5, 6, 7, 13], [40, 60, 70]], {(1, 2), (0, 40)})

    spc.set_equal(0, 1)
    assert spc == SetPartComp([[0, 1, 8, 9, 10, 20, 30, 50], [2, 3, 4, 11, 12, 40, 60, 70], [5, 6, 7, 13]], {(0, 2)})

    spc.set_equal(2, 5)
    assert spc == SetPartComp([[0, 1, 8, 9, 10, 20, 30, 50], [2, 3, 4, 5, 6, 7, 11, 12, 13, 40, 60, 70]], {(0, 2)})


def test_canonical_comp_pairs():
    a = SetPartComp([[1, 3], [5, 7]], {(1, 5)})
    b = SetPartComp([[1, 3], [5, 7]], {(1, 7)})
    c = SetPartComp([[1, 3], [5, 7]], {(3, 5)})
    d = SetPartComp([[1, 3], [5, 7]], {(3, 7)})
    e = SetPartComp([[1, 3], [5, 7]], {(7, 3)})
    assert a == b == c == d == e
    assert a.comp_pairs == b.comp_pairs == c.comp_pairs == d.comp_pairs == e.comp_pairs == {(1, 5)}
