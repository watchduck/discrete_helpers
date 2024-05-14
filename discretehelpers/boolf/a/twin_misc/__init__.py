from discretehelpers.a import int_to_exposet, exposet_to_int, linear_to_walsh_and_oddness
from discretehelpers.boolf.a import atoms_to_and_gen, atoms_to_xand_gen
from discretehelpers.binv import Binv


"""
'conju' stands for 'conjunction' (logical AND).
It comes from the Zhegalkin functions, but is a misnomer for the prefect functions.
"""


# raw generators #######################################################################################################

def raw_tt_gen(tt, conju_gen, arity):
    if type(tt) == str:
        tt = [int(_) for _ in tt.replace(' ', '')]
    assert len(tt) == 1 << arity  # 2 ** arity
    if sum(tt):  # if the truth table contains at least one true entry
        conjus = [conju_gen(int_to_exposet(k), arity) for k, v in enumerate(tt) if v]
        zipped_conjus = zip(*conjus)
        for binary_tuple in zipped_conjus:
            yield sum(binary_tuple) % 2
    else:  # if the truth table contains only false entries
        for _ in tt:
            yield 0


def raw_exposet_gen(exposet, conju_gen, arity):
    conjus = [conju_gen(int_to_exposet(green_place), arity) for green_place in exposet]
    zipped_conjus = zip(*conjus)
    for red_place, binary_tuple in enumerate(zipped_conjus):
        if sum(binary_tuple) % 2:
            yield red_place


# Zhegalkin stuff with AND (`conju_gen` is `atoms_to_and_gen`.) ########################################################

def vector_to_twin_gen(tt, arity):
    return raw_tt_gen(tt, atoms_to_and_gen, arity)


def exposet_to_twin_gen(exposet, arity):
    return raw_exposet_gen(exposet, atoms_to_and_gen, arity)


def twin_int(i, arity):
    exposet_i = int_to_exposet(i)
    exposet_result_gen = exposet_to_twin_gen(exposet_i, arity)
    return exposet_to_int(exposet_result_gen)


# prefect stuff with XAND (`conju_gen` is `atoms_to_xand_gen`.) ########################################################

def zhe_vector_to_prefect_gen(tt, arity):
    return raw_tt_gen(tt, atoms_to_xand_gen, arity)


def zhe_exposet_to_prefect_gen(exposet, arity):
    return raw_exposet_gen(exposet, atoms_to_xand_gen, arity)


def zhe_to_prefect(n, arity):
    length = 1 << arity
    binv = Binv(intval=n, length=length)
    vector_result_gen = zhe_vector_to_prefect_gen(binv, arity)
    return linear_to_walsh_and_oddness(list(vector_result_gen))
