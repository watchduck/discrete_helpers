from discretehelpers.a import int_to_exposet
from discretehelpers.set_part import SetPart

from .atom_partition import atom_partition


def sierpinski_partition(n, arity):

    exposet = int_to_exposet(n)

    result = SetPart()

    for atomval in exposet:
        result = result.join(
            atom_partition(atomval, arity)
        )

    return result
