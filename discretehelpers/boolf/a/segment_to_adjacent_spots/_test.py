from . import segment_to_adjacent_spots


def test():

    vector = (-1, 1, 0, 0)  # −+00
    assert segment_to_adjacent_spots(vector) == [2, 6, 10, 14]  # 0100, 0101, 0110, 0111
