from . import abbrev_testing
from .ex import *


def test_raise():
    abbrev_testing(NoArgError, [
        lambda: Hand()
    ])

    abbrev_testing(NotFiveError, [
        lambda: Hand(0),
        lambda: Hand(6),
        lambda: Hand(''),
        lambda: Hand('5')
    ])


def test_values():
    abbrev_testing(10, [
        Hand(5).twice_five
    ])


# example class
class Hand:
    def __init__(self, give_me_five=None):
        if give_me_five is None:
            raise NoArgError
        if give_me_five != 5:
            raise NotFiveError
        self.twice_five = 2 * give_me_five
