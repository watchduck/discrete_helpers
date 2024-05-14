from . import spread_sigperm_to_sigvar


def test():

    assert spread_sigperm_to_sigvar([ 0,  1,  2,  3], [ 0,  0,  5,  5]) == [ 0,  1,  7,  8]
    assert spread_sigperm_to_sigvar([ 0,  1, ~2,  3], [ 0,  0,  5,  5]) == [ 0,  1, ~7,  8]
    assert spread_sigperm_to_sigvar([~0,  1, ~2,  3], [ 0,  0,  5,  5]) == [~0,  1, ~7,  8]
    assert spread_sigperm_to_sigvar([~0,  1, ~2,  3], [ 0,  0,  5,  5]) == [~0,  1, ~7,  8]

    assert spread_sigperm_to_sigvar([ 1,  3,  0,  2], [ 0,  0,  5,  5]) == [ 1,  8,  0,  7]
    assert spread_sigperm_to_sigvar([ 1, ~3,  0,  2], [ 0,  0,  5,  5]) == [ 1, ~8,  0,  7]

