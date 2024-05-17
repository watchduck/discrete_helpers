from functools import cached_property

from discretehelpers.a import true_except

from ...ex import DomainNotFiniteError


@cached_property
def singletons(self):

    true_except(type(self.domain) == set, DomainNotFiniteError)

    result = self.domain.difference(self.non_singletons)

    return result
