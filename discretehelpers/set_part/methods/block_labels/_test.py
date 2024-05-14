from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.set_part import SetPart

from .ex import LabelContradictionError, UnknownBlockError


def test_simple():
    p = SetPart([[3, 5], [7, 9]])

    assert p.canonical_blocks_with_singletons == [[0], [1], [2], [3, 5], [4], [6], [7, 9], [8]]

    abbrev(UnknownBlockError, [
        lambda: p.add_label_to_block([2, 5], 'wrong block'),
        lambda: p.add_label_to_block([10], 'too big singleton')
    ])

    p.add_label_to_block([3, 5], 'small')
    p.add_label_to_block([7, 9], 'big')

    abbrev(LabelContradictionError, [
        lambda: p.add_label_to_block([7, 9], 'medium'),  # already called 'big'
        lambda: p.merge_pair(3, 9)  # contradicting labels 'small' and 'big'
    ])

    p.add_label_to_block([6], 'medium')

    assert p.block_labels == {(3, 5): 'small', (6,): 'medium', (7, 9): 'big'}

    assert p.get_label_from_block([3, 5]) == 'small'
    assert p.get_block_from_label('big') == [7, 9]

    assert p.get_label_from_element(3) == 'small'
    assert p.get_label_from_element(5) == 'small'

    assert p.get_block_from_element(3) == [3, 5]
    assert p.get_block_from_element(5) == [3, 5]


def test_merge():
    p = SetPart([[3, 5], [7, 9]])

    p.add_label_to_element(5, 'foo')
    assert dict(p.block_labels) == {(3, 5): 'foo'}

    p.merge_pair(3, 9)
    assert dict(p.block_labels) == {(3, 5, 7, 9): 'foo'}

    p.add_label_to_element(8, 'bar')
    assert dict(p.block_labels) == {(3, 5, 7, 9): 'foo', (8,): 'bar'}
