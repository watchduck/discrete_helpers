from functools import cached_property

from discretehelpers.a import linear_to_walsh_and_oddness
from discretehelpers.a.walsh_function_to_index.ex import NotWalshRowError


@cached_property
def is_linear(self):

    try:
        linear_to_walsh_and_oddness(self.dense_tt)
        return True
    except NotWalshRowError:
        return False
