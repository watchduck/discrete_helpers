from itertools import product, combinations
from math import factorial

from discretehelpers.a import have, true_except, rev_colex_perms
from discretehelpers.binv import Binv
from discretehelpers.perm import Perm
from discretehelpers.sig_perm import SigPerm
from discretehelpers.set_part import SetPart

from discretehelpers.ex import ArgTooSmallError, ArgNotFeasibleError


def ec_clan(self, arity=None, suppress_abbreviation=False):

    if self.is_constant:
        if not suppress_abbreviation:
            pair_or_triple = (0, 0) if not arity else (0, 0, 0)
            part = SetPart(blocks=[], domain={pair_or_triple})
            part.add_label_to_element(pair_or_triple, self)
            return part
        else:
            from discretehelpers.boolf import Boolf
            fullspots = list(range(2 ** arity)) if self.root[0] else []
            atomvals = list(range(arity))
            boolf = Boolf(fullspots=fullspots, atomvals=atomvals, skip_deflation=True)
            return boolf.ec_clan(arity, suppress_abbreviation)

    true_except(self.adicity <= 5, ArgNotFeasibleError)

    if not have(arity):
        arity = self.adicity
    else:
        true_except(arity >= self.adicity, ArgTooSmallError)

    if arity == self.valency:
        case = 'redundant'
    else:
        if suppress_abbreviation:
            case = 'redundant'
        else:
            case = 'abbreviated'

    if case == 'redundant':

        arity_power = 2 ** arity
        arity_factorial = factorial(arity)

        perms_raw = rev_colex_perms(arity)
        perms = [Perm(list(_)) for _ in perms_raw]
        binvs = [Binv(intval=_) for _ in range(arity_power)]

        pairs_m_n = list(product(range(arity_power), range(arity_factorial)))

        part = SetPart(blocks=[], domain=pairs_m_n)
        for m, binv in enumerate(binvs):
            for n, perm in enumerate(perms):
                sigperm = SigPerm(valneg=binvs[m], perm=perms[n])
                boolf = self.apply_sigperm(sigperm)
                part.add_label_to_element(element=(m, n), label=boolf)

    elif case == 'abbreviated':

        combos = list(combinations(range(arity), self.valency))  # valency-element subsets of range(arity)
        arity_choose_valency = len(combos)

        valency_power = 2 ** self.valency
        valency_factorial = factorial(self.valency)

        perms_raw = rev_colex_perms(self.valency)
        perms = [Perm(list(_)) for _ in perms_raw]
        binvs = [Binv(intval=_) for _ in range(valency_power)]

        triples_m_n_c = list(product(range(valency_power), range(valency_factorial), range(arity_choose_valency)))

        part = SetPart(blocks=[], domain=triples_m_n_c)
        for c, combo in enumerate(combos):
            for m, binv in enumerate(binvs):
                for n, perm in enumerate(perms):
                    sigperm = SigPerm(valneg=binvs[m], perm=perms[n])
                    signed_variation = sigperm.apply_on_vector(combo)
                    boolf = self.apply(*signed_variation)
                    part.add_label_to_element(element=(m, n, c), label=boolf)

        part.glove_compartment = combos

    return part
