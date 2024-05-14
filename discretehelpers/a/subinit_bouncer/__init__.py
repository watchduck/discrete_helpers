from discretehelpers.a import have


def subinit_bouncer(self, required_keys, optional_keys=None):

    """
    :param self: Boolf object
    :param required_keys: list of required keys to `self._doa`
    :param optional_keys: list of optional keys to `self._doa`
    :return: boolean: `self._doa[key]` is something (not None) for required, nothing (None) for forbidden keys
    """

    for key in required_keys:
        if self._doa[key] is None:
            return False

    all_keys = set(self._doa.keys())
    required_keys = set(required_keys)
    optional_keys = set(optional_keys) if have(optional_keys) else set()

    assert required_keys.issubset(all_keys)
    assert optional_keys.issubset(all_keys)
    assert not required_keys.intersection(optional_keys)
    
    allowed_keys = required_keys.union(optional_keys)
    forbidden_keys = all_keys.difference(allowed_keys)
    for key in forbidden_keys:
        if self._doa[key] is not None:
            return False

    return True
