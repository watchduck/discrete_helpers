from discretehelpers.boolf import Boolf


# grid sides
t9_grid_boolf_abcd = Boolf('1011 1000 0000 1000', [0, 1, 2, 3])
t9_grid_boolf_abd = Boolf('1011 1000', [0, 1, 3])
t9_grid_boolf_efgh = Boolf('1101 0001 0000 0001', [4, 5, 6, 7])


# fullspots

# 5 × 5 (based on medina)
medina_fs = {0, 2, 3, 4, 12, 16, 18, 19, 20, 28, 48, 50, 51, 52, 60, 112, 114, 115, 116, 124, 240, 242, 243, 244, 252}
gunumi_fs = {3, 51, 243, 18, 114, 0, 48, 240, 116, 20, 252, 60, 12}
deginu_fs = {0, 2, 3, 19, 51, 115, 243, 242, 240, 252, 20, 52, 116, 12}

# 5 × 5 changed shape
pomote_fs = medina_fs.difference(gunumi_fs)
gulivu_fs = {0, 16, 20, 52, 116, 112, 114, 50, 51, 243, 252}
filege_fs = {2, 18, 50, 51, 115, 242, 48, 112, 116, 252, 124, 60, 20, 12}
bukoru_fs = {2, 12, 16, 20, 50, 115, 112, 116, 243, 242, 240}
dukamu_fs = medina_fs.difference({48, 242, 243, 124, 12})
ligoba_fs = medina_fs.difference({0, 3, 19, 51, 48, 116, 12, 28, 60})
pirake_fs = {19, 51, 50, 114, 16, 244, 60, 4, 12}
gatade_fs = medina_fs.difference({18, 19, 50, 51, 114, 115, 242, 243, 4, 12})

# 5 × 5 with one-sided splits
tinefa_fs = {16, 18, 19, 48, 51, 52, 112, 114, 115}

# 5 × 4 (based on manila)
manila_bloated_fs = medina_fs.difference({0, 16, 48, 112, 240})
manila_fs = {0, 2, 3, 4, 8, 10, 11, 12, 24, 26, 27, 28, 56, 58, 59, 60, 120, 122, 123, 124}

nafega_fs = {2, 3, 8, 24, 56, 122, 123, 124, 4}
takeli_fs = manila_fs.difference({8, 24, 56, 120})
tevoga_fs = {3, 11, 27, 59, 123, 122, 120, 124, 60, 28, 12, 4}
luvati_fs = manila_fs.difference({10, 26, 58, 56, 12})

# 5 × 4 changed shape
karifu_fs = {2, 4, 8, 11, 26, 28, 56, 59, 122, 124}
linaki_fs = manila_fs.difference(karifu_fs)
bokivi_fs = manila_fs.difference({2, 3, 26, 27, 58, 59, 60, 12, 4})
nitevu_fs = {0, 10, 11, 26, 27, 58, 59, 60, 124}
numado_fs = manila_fs.difference({10, 26, 58, 56, 12, 4})
sigovu_fs = {2, 27, 26, 24, 123, 122, 120, 60, 12}
nogoka_fs = {2, 10, 11, 27, 59, 58, 56, 24, 28, 12, 122}
nusure_fs = {2, 10, 11, 27, 59, 58, 56, 24, 28, 12, 120}

# 5 × 4 with one-sided splits
gufaro_fs = {2, 10, 11, 12, 24, 27, 28, 56, 58, 59}
temapi_fs = {8, 24, 56, 120}


# functions to initialize the Boolean functions

def _a_init(fs):
    return Boolf(fullspots=fs, atomvals=list(range(8)))


def _b_init(fs):
    return Boolf(fullspots=fs, atomvals=[0, 1, 3, 4, 5, 6, 7])


# Boolean functions

medina = _a_init(medina_fs)
gunumi = _a_init(gunumi_fs)
deginu = _a_init(deginu_fs)

pomote = _a_init(pomote_fs)
gulivu = _a_init(gulivu_fs)
filege = _a_init(filege_fs)
bukoru = _a_init(bukoru_fs)
dukamu = _a_init(dukamu_fs)
ligoba = _a_init(ligoba_fs)
pirake = _a_init(pirake_fs)
gatade = _a_init(gatade_fs)

tinefa = _a_init(tinefa_fs)

manila_bloated = _a_init(manila_bloated_fs)  # `_a_init` instead of `_b_init`

manila = _b_init(manila_fs)
nafega = _b_init(nafega_fs)
takeli = _b_init(takeli_fs)
tevoga = _b_init(tevoga_fs)
luvati = _b_init(luvati_fs)

linaki = _b_init(linaki_fs)
karifu = _b_init(karifu_fs)
bokivi = _b_init(bokivi_fs)
nitevu = _b_init(nitevu_fs)
numado = _b_init(numado_fs)
sigovu = _b_init(sigovu_fs)
nogoka = _b_init(nogoka_fs)
nusure = _b_init(nusure_fs)

gufaro = _b_init(gufaro_fs)
temapi = _b_init(temapi_fs)
