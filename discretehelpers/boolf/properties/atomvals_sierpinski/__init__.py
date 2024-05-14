from functools import cached_property

from discretehelpers.a import int_to_sierpinski_row


@cached_property
def atomvals_sierpinski(self):

    return int_to_sierpinski_row(exposet=self.atomvals)
