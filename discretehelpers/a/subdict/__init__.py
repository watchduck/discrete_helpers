from .. import have


def subdict(original, drop=None, fresh=None):

    result = dict()

    kept_keys = set(original.keys())
    if have(drop):
        kept_keys = kept_keys.difference(set(drop))
    if have(fresh):
        kept_keys = kept_keys.difference(set(fresh.keys()))

    for key in kept_keys:
        result[key] = original[key]

    for key, val in fresh.items():
        result[key] = val

    return result
