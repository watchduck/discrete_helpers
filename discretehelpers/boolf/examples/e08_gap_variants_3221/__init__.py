from discretehelpers.boolf import Boolf


def _formula(var_abc, var_de, var_fg, var_h):
    abc = Boolf(var_abc, [0, 1, 2])
    de = Boolf(var_de, [3, 4])
    fg = Boolf(var_fg, [5, 6])
    h = Boolf(var_h, [7])

    return (abc & _frame_abc) | (de & _frame_de) | (fg & _frame_fg) | (h & _frame_h)


# based on kusaru
_frame_abc = Boolf(multi_and=[~3, ~4, ~5, ~6, ~7])
_frame_de = Boolf(multi_and=[~0, ~1, ~2, ~5, ~6, ~7])
_frame_fg = Boolf(multi_and=[~0, ~1, ~2, ~3, ~4, ~7])
_frame_h = Boolf(multi_and=[~0, ~1, ~2, ~3, ~4, ~5, ~6])

kusaru = _formula('1111 1111', '1111', '1111', '11')
sasunu = _formula('0111 1111', '0111', '0111', '01')
banatu = _formula('1110 1001', '1111', '1111', '11')


# based on lekate
_frame_abc = Boolf(multi_and=[~3, ~4, ~5, ~6, ~7])
_frame_de = Boolf(multi_and=[~0, 1, ~2, ~5, ~6, 7])
_frame_fg = Boolf(multi_and=[~0, 1, 2, ~3, ~4, ~7])
_frame_h = Boolf(multi_and=[~0, 1, ~2, ~3, ~4, ~5, ~6])

lekate = _formula('1111 1111', '1111', '1111', '11')
vepane = _formula('1111 1100', '0111', '0111', '10')
nutite = _formula('1101 1111', '0111', '1111', '00')


# based on lobeva
_frame_abc = Boolf(multi_and=[~3, ~4, 5, ~6, 7])
_frame_de = Boolf(multi_and=[~0, ~1, ~2, ~5, 6, 7])
_frame_fg = Boolf(multi_and=[~0, ~1, ~2, ~3, ~4, 7])
_frame_h = Boolf(multi_and=[~0, ~1, ~2, ~3, ~4, ~5, ~6])

lobeva = _formula('1111 1111', '1111', '1111', '11')
tigola = _formula('0111 1110', '0111', '1001', '11')

karato = _formula('1101 0001', '1101', '1110', '11')
karafa = _formula('1110 0001', '1011', '0110', '10')
todeda = _formula('1011 0101', '1101', '0111', '00')
lapava = _formula('0111 1111', '0111', '1001', '01')

todeda_blightless = todeda.blightless_boolf
lapava_blightless = lapava.blightless_boolf
