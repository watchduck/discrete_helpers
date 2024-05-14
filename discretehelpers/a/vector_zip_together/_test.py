from discretehelpers.a import abbrev_testing as abbrev

from . import vector_zip_together


def test_results():

    assert vector_zip_together([[10, 12, 14], [11, 13], [15]], [0, 1, 0, 1, 0, 2]) == [10, 11, 12, 13, 14, 15]
    assert vector_zip_together([['a', 'c'], ['b']], [0, 1, 0]) == ['a', 'b', 'c']
