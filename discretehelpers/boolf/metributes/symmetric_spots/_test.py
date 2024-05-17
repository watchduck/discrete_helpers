from discretehelpers.set_part import SetPart
from discretehelpers.boolf.examples import niliko, tabita, levana, dukeli


def test():

    assert niliko.symmetric_spots == SetPart([[0, 12], [1, 14], [5, 6], [9, 10]], {0, 1, 4, 5, 6, 7, 8, 9, 10, 12, 14})

    assert tabita.symmetric_spots == SetPart([[2, 4, 8], [3, 5, 9], [6, 10, 12], [7, 11, 13]], {0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13})

    assert levana.symmetric_spots == SetPart([[0, 1], [2, 3], [4, 9], [5, 8], [7, 10]], {0, 1, 2, 3, 4, 5, 7, 8, 9, 10})

    assert dukeli.symmetric_spots == SetPart([[1, 8], [2, 4], [3, 12]], {0, 1, 2, 3, 4, 6, 8, 12})
    assert dukeli.symmetric_spots.blocks_with_singletons() == [[0], [1, 8], [2, 4], [3, 12], [6]]
