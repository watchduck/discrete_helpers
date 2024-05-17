from functools import cached_property

"""
`self.bloat` uses atomkeys instead of atomvals. But the latter are used here.
"""


@cached_property
def bloat_boolf(self):
    from discretehelpers.boolf import Boolf

    boolf_with_atom_places = self.bloat.boolf()
    selection_of_atom_places = boolf_with_atom_places.atomvals
    selection_of_atomvals = [self.atomvals[_] for _ in selection_of_atom_places]
    return Boolf(boolf_with_atom_places.dense_tt, selection_of_atomvals)
