from discretehelpers.a import true_except, logic_negate_vector
from discretehelpers.binv import Binv
from discretehelpers.set_part import SetPart

from discretehelpers.ex import ArgNotFeasibleError


def ec_family(self):

    if self.is_constant:
        part = SetPart(blocks=[], domain={0})
        part.add_label_to_element(0, self)
        return part

    true_except(self.adicity <= 10, ArgNotFeasibleError)

    valency_power = 2 ** self.valency

    domain = list(range(valency_power))
    part = SetPart(blocks=[], domain=domain)
    for i in range(valency_power):
        negpat_raw = Binv(intval=i, length=self.valency).exposet  # negator pattern
        negpat = [self.atomvals[_] for _ in negpat_raw]
        signed_atomvals = logic_negate_vector(self.atomvals, which=negpat)
        boolf = self.apply(*signed_atomvals)
        part.add_label_to_element(element=i, label=boolf)

    return part
