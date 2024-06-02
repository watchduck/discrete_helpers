import pytest

from discretehelpers.set_part import SetPart


@pytest.mark.parametrize('case', [
    {
        'a': SetPart([[0, 1, 2, 4], [5, 6, 9], [7, 8]]),
        'b': SetPart([[0, 1], [2, 3, 4], [6, 8, 9]]),
        'meet': SetPart([[0, 1], [2, 4], [6, 9]]),
        'join': SetPart([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
    },
    {
        'a': SetPart([[1, 4, 6], [2, 3, 5], [8, 9, 10, 11]]),
        'b': SetPart([[2, 3], [4, 5], [7, 8]]),
        'meet': SetPart([[2, 3]]),
        'join': SetPart([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11]])
    },
    {
        'a': SetPart([[4, 7, 9], [2, 1, 0], [2, 6, 5, 10]]),
        'b': SetPart([[1, 2, 3], [4, 5], [10, 11, 12]]),
        'meet': SetPart([[1, 2]]),
        'join': SetPart([[0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12]])
    },
    {
        'a': SetPart(),
        'b': SetPart([[1, 3]]),
        'meet': SetPart(),
        'join': SetPart([[1, 3]])
    },
    {
        'a': SetPart([[1, 2], [5, 6, 7], [10, 20]]),
        'b': SetPart([[1, 2], [4, 6, 9], [10, 11]]),
        'meet': SetPart([[1, 2]]),
        'join': SetPart([[1, 2], [4, 5, 6, 7, 9], [10, 11, 20]])
    },
    {
        'a': SetPart([[1, 2], [5, 6, 7], [10, 20, 30]]),
        'b': SetPart([[1, 2], [4, 6, 9], [10, 11, 30]]),
        'meet': SetPart([[1, 2], [10, 30]]),
        'join': SetPart([[1, 2], [4, 5, 6, 7, 9], [10, 11, 20, 30]])
    }
])
def test(case):
    a, b, meet, join = [case[_] for _ in ['a', 'b', 'meet', 'join']]

    assert a._meet_prototype(b) == meet

    assert a.meet(b) == meet
    assert b.meet(a) == meet

    assert a.join(b) == join
    assert b.join(a) == join
