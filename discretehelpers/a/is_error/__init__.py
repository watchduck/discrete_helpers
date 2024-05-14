from inspect import isclass


def is_error(candidate):
    return isclass(candidate) and issubclass(candidate, Exception)
