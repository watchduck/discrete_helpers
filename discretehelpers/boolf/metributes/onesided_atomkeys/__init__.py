from functools import cached_property


@cached_property
def onesided_atomkeys(self):

    result = []
    for atomkey, split_is_onesided in enumerate(self.splits_onesided):
        if split_is_onesided:
            result.append(atomkey)

    return result
