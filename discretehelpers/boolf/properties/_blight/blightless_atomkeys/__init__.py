from functools import cached_property


@cached_property
def blightless_atomkeys(self):

    bloatless_atomkeys_deflated = set(self.bloatless_atomkeys_deflated)
    onesided_atomkeys = set(self.onesided_atomkeys)

    result = sorted(bloatless_atomkeys_deflated.difference(onesided_atomkeys))

    return result
