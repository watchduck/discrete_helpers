from discretehelpers.boolf.a import apply_sigperm_to_colors


def test():

    kisago_colors = {
        'r': [6, 7, 10, 11],
        'g': [4, 5, 8, 9],
        'y':  [1, 12]
    }

    kisegi_colors = {
        'r': [0, 1, 12, 13],
        'g': [2, 3, 14, 15],
        'y': [7, 10]
    }

    sigperm = [0, ~1, ~2, 3]

    assert apply_sigperm_to_colors(kisago_colors, 4, sigperm) == kisegi_colors
