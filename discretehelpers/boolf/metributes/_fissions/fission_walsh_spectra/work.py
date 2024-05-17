from sympy import fwht  # fast Walsh-Hadamard transform (Walsh spectrum)

from discretehelpers.boolf.a import flat_to_layered


def work(self):

    result_signed_flat = []
    result_abs_flat = []
    result_signed_layered = []
    result_abs_layered = []

    for a, b in self.fissions:

        # conversions from `Binv` objects to binary vectors
        a = [int(_) for _ in a]
        b = [int(_) for _ in b]

        # conversion to Walsh spectra
        wa = tuple(fwht(a))
        wb = tuple(fwht(b))

        # absolute values
        wa_abs = tuple([abs(_) for _ in wa])
        wb_abs = tuple([abs(_) for _ in wb])

        # append layered versions to results

        result_signed_flat.append([wa, wb])
        result_abs_flat.append([wa_abs, wb_abs])
        result_signed_layered.append([flat_to_layered(wa), flat_to_layered(wb)])
        result_abs_layered.append([flat_to_layered(wa_abs), flat_to_layered(wb_abs)])

    self.fission_walsh_spectra = result_signed_flat
    self.fission_walsh_spectra_abs = result_abs_flat
    self.fission_walsh_spectra_layered = result_signed_layered
    self.fission_walsh_spectra_layered_abs = result_abs_layered

    return result_signed_flat, result_abs_flat, result_signed_layered, result_abs_layered
