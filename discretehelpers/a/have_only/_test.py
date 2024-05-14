from discretehelpers.a import abbrev_testing as abbrev
from discretehelpers.ex import ArgComboError

from . import have_only


a = 1
b = 2
c = None
d = None
all_args = [a, b, c, d]


def test():

    assert have_only([a, b], all_args)

    assert not have_only([a, b, c], all_args)

    abbrev(ArgComboError, [
        lambda: have_only([a], all_args)
    ])
