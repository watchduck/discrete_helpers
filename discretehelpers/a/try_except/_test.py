from discretehelpers.a import abbrev_testing as abbrev

from . import try_except


def test():
    abbrev(SpecificError, [
        lambda: try_except(lambda: 0 / 0, do_raise=SpecificError, if_raised=ZeroDivisionError),
        lambda: try_except(lambda: 1 / 0, do_raise=SpecificError, if_raised=ZeroDivisionError)
    ])
    abbrev(GeneralError, [
        lambda: try_except(lambda: 0 / 0, do_raise=GeneralError),
        lambda: try_except(lambda: 1 / 0, do_raise=GeneralError)
    ])


class SpecificError(ZeroDivisionError):
    """my zero division error"""


class GeneralError(Exception):
    """my unspecific error"""
