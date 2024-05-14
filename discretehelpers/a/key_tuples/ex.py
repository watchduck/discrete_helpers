class ArgNotContainerError(ValueError):
    """The argument is not a list or a dictionary."""


class ItemNotContainerFail(Exception):
    """The item (in the list or dictionary) is itself not a list or a dictionary. (used for control flow)"""


class ItemEmptyContainerFail(Exception):
    """The item (in the list or dictionary) is itself an empty list or an empty dictionary. (used for control flow)"""
