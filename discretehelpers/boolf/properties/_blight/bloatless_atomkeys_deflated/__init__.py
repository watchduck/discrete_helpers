from functools import cached_property


@cached_property
def bloatless_atomkeys_deflated(self):

    bloatless_atomvals = self.bloatless_boolf.atomvals
    result = [key for key, val in enumerate(self.atomvals) if val in bloatless_atomvals]

    return result
