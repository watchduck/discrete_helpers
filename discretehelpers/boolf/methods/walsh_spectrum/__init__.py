from sympy import fwht
from discretehelpers.boolf.a import flat_to_layered


def walsh_spectrum(self, arg=None):
    tt = [int(_) for _ in self.tt(arg)]
    result_list = [int(_) for _ in fwht(tt)]  # get rid of SymPy datatype
    return tuple(result_list)


def walsh_spectrum_abs(self, arg=None):
    ws = self.walsh_spectrum(arg)
    return tuple([abs(_) for _ in ws])


#############################################################


def walsh_spectrum_layered(self, arg=None):
    ws = self.walsh_spectrum(arg)
    return flat_to_layered(ws)


def walsh_spectrum_abs_layered(self, arg=None):
    ws_abs = self.walsh_spectrum_abs(arg)
    return flat_to_layered(ws_abs)
