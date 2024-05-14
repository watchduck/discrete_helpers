from discretehelpers.boolf.examples import tokosi


def test():

    # atomvals
    assert tokosi.filtrated_pairs_pretty(tokosi.atomvals) == {
        'complementary': [(3, 7), (3, 9)],
        'equal': [(7, 9)],
        'crossing': [(1, 3), (1, 5), (1, 7), (1, 9), (3, 5), (5, 7), (5, 9)]
    }

    # atomnames (border colors)
    assert tokosi.filtrated_pairs_pretty(['red', 'green', 'blue', 'brown', 'orange']) == {
        'complementary': [('green', 'brown'), ('green', 'orange')],
        'equal': [('brown', 'orange')],
        'crossing': [('red', 'green'), ('red', 'blue'), ('red', 'brown'), ('red', 'orange'), ('green', 'blue'), ('blue', 'brown'), ('blue', 'orange')]
    }
