from functools import cached_property

from discretehelpers.binv import Binv
from discretehelpers.a import linear_to_walsh_and_oddness, linear_to_leader_and_quadrant
from discretehelpers.boolf.a import vector_to_twin_gen, zhe_vector_to_prefect_gen


@cached_property
def prefect_tt(self):

    twin_tt = list(
        vector_to_twin_gen(
            self.tt(),
            self.adicity
        )
    )

    return Binv(list(
        zhe_vector_to_prefect_gen(
            twin_tt,
            self.adicity
        )
    ))


@cached_property
def prefect_boolf(self):
    from discretehelpers.boolf import Boolf

    return Boolf(self.prefect_tt)


@cached_property
def prefect_walsh_and_oddness(self):
    return linear_to_walsh_and_oddness(self.prefect_tt)


@cached_property
def prefect_leader_and_quadrant(self):
    return linear_to_leader_and_quadrant(self.prefect_tt)
