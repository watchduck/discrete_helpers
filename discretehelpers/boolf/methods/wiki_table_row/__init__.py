import os

from string import Template

from discretehelpers.a import true_except, decimal_length

from .ex import BlightError, SpreadError, VFractERROR


file_path = os.path.join(
    os.path.dirname(__file__),
    'string.txt'
)


def wiki_table_row(self, names_cell):

    true_except(self.is_blightless, BlightError)
    true_except(self.is_root, SpreadError)

    vfract = self.value_fract()
    wfract = self.weight_fract

    vinterval = 'below-half' if vfract < .5 else 'above-half'
    true_except(vfract != .5, VFractERROR)

    if wfract < .5:
        winterval = 'below-half'
    elif wfract == .5:
        winterval = 'exactly-half'
    elif wfract > .5:
        winterval = 'above-half'

    vnum = vfract.numerator
    vden = vfract.denominator

    vnum_len = decimal_length(vnum)
    vden_len = decimal_length(vden)

    if vnum_len > 30 or vden_len > 30:
        fraction_font_size = 'smaller'
    elif vnum_len > 15 or vden_len > 15:
        fraction_font_size = 'small'
    else:
        fraction_font_size = ''

    wnum = wfract.numerator
    wden = wfract.denominator

    length = 2 ** self.valency
    reducing_factor = length / wden

    wnum_big = int(wnum * reducing_factor)

    vdec = format(vnum / vden, '.20f')[1::]  # with trailing zeros
    wdec = format(wnum / wden, '.20g')[1::]  # without trailing zeros

    zhegalkin = self.zhe
    zhegalkin_len = decimal_length(zhegalkin)

    zhegalkin_oddness = 'odd' if zhegalkin % 2 else 'even'

    if zhegalkin_len > 30:
        zhegalkin_font_size = 'smaller'
    elif zhegalkin_len > 15:
        zhegalkin_font_size = 'small'
    else:
        zhegalkin_font_size = ''

    d = {
        'zhegalkin': zhegalkin,
        'zhegalkin_oddness': zhegalkin_oddness,
        'zhegalkin_font_size': zhegalkin_font_size,
        'vnum': vnum, 'vden': vden, 'vdec': vdec, 'vinterval': vinterval,
        'wnum': wnum, 'wden': wden, 'wdec': wdec, 'winterval': winterval,
        'wnum_big': wnum_big, 'wden_big': length,
        'valency': self.valency,
        'fraction_font_size': fraction_font_size,
        'names_cell': names_cell,
        'number_of_bundles': len(self.bundles),
        'unibundle_class': ' uni' if len(self.bundles) == 1 else ''
    }

    with open(file_path, 'r') as f:
        src = Template(f.read())
        result = src.substitute(d)
        return result
