from . import count_split_regions


def test():
    assert count_split_regions(({1, 3}, {0, 8, 6}), ({3, 6}, {0, 1, 8})) == 4
    assert count_split_regions(({1, 3}, {0, 8, 6}), ({6}, {0, 1, 3, 8})) == 3
