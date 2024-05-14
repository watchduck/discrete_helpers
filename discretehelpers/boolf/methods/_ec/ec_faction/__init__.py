from itertools import product, combinations
from math import factorial

from discretehelpers.a import have, true_except, rev_colex_perms
from discretehelpers.perm import Perm
from discretehelpers.set_part import SetPart

from discretehelpers.ex import ArgTooSmallError, ArgNotFeasibleError


def ec_faction(self, arity=None, suppress_abbreviation=False):

    if self.is_constant:
        if not have(arity):
            arity = 0
        if suppress_abbreviation and arity > 0:
            domain = set(range(factorial(arity)))
            part = SetPart(blocks=[domain], domain=domain)
            part.add_label_to_element(0, self)
            return part
        int_or_pair = 0 if arity == 0 else (0, 0)
        part = SetPart(blocks=[[int_or_pair]], domain={int_or_pair})
        part.add_label_to_element(int_or_pair, self)
        return part

    true_except(self.adicity <= 5, ArgNotFeasibleError)

    if not have(arity):
        arity = self.adicity
    else:
        true_except(arity >= self.adicity, ArgTooSmallError)

    if arity == self.valency:
        case = 'short'
    else:
        if suppress_abbreviation:
            case = 'short'
        else:
            case = 'long'

    if case == 'short':

        perms = rev_colex_perms(arity)
        perm_exposet = list(range(factorial(arity)))

        part = SetPart(blocks=[], domain=perm_exposet)
        for n, perm in enumerate(perms):
            boolf = self.apply_sigperm(perm)
            part.add_label_to_element(element=n, label=boolf)

    elif case == 'long':

        combos = list(combinations(range(arity), self.valency))  # valency-element subsets of range(arity)
        arity_choose_valency = len(combos)
        combo_exposet = list(range(arity_choose_valency))

        perms = rev_colex_perms(self.valency)
        perm_exposet = list(range(factorial(self.valency)))

        pairs_n_c = list(product(perm_exposet, combo_exposet))

        part = SetPart(blocks=[], domain=pairs_n_c)
        for c, combo in enumerate(combos):
            for n, perm in enumerate(perms):
                variation = Perm(perm).apply_on_vector(combo)
                boolf = self.apply(*variation)
                part.add_label_to_element(element=(n, c), label=boolf)

        part.glove_compartment = combos

    return part
