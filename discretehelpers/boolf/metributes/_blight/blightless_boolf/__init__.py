from functools import cached_property


@cached_property
def blightless_boolf(self):
    from discretehelpers.boolf import Boolf

    if self.is_constant:
        return self
    if self.blight_boolf == self:
        return Boolf('1')
    else:
        blightless_atomvals = [self.atomvals[_] for _ in self.blightless_atomkeys]
        return self.bloatless_boolf.filtrated_boolf(blightless_atomvals)
