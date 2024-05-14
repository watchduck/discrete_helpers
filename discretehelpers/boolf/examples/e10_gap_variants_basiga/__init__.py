from discretehelpers.boolf import Boolf

from discretehelpers.boolf.examples import basiga_fs


# fullspots blightless
torova_fs = {1, 2, 4, 7, 8, 14, 26, 28, 42, 74, 138}
kulika_fs = basiga_fs.difference(torova_fs)
doguva_fs = basiga_fs.difference({7, 10, 26})
sarina_fs = basiga_fs.difference({5, 7, 12, 14, 28, 30, 42, 74, 138})
dinado_fs = basiga_fs.difference({3, 4, 5, 6, 10, 30, 42})
giteli_fs = basiga_fs.difference({6, 7, 14, 30})
kokabi_fs = {0, 2, 5, 6, 7, 14, 26, 28, 30, 42, 74, 202}
teloti_fs = basiga_fs.difference({0, 7, 10, 30, 106, 202})
pamoda_fs = basiga_fs.difference({3, 7, 10, 12, 14, 24, 42, 202})
tomute_fs = {0, 3, 5, 7, 10, 28, 30, 42, 106, 202}
vumali_fs = {2, 3, 5, 7, 30, 28, 10, 42, 106, 202}

# fullspots blighted
futare_fs = {7, 24, 106, 202}
geteso_fs = {2, 5, 6, 30, 42, 202}
bitada_fs = {2, 7, 10, 26, 74, 138}
duvola_fs = {7, 10, 26, 74, 138}


# function to initialize the Boolean functions

def init(fullspots):
    return Boolf(fullspots=fullspots, atomvals=list(range(8)))


# Boolean functions

kulika = init(kulika_fs)
torova = init(torova_fs)
doguva = init(doguva_fs)
sarina = init(sarina_fs)
dinado = init(dinado_fs)
giteli = init(giteli_fs)
kokabi = init(kokabi_fs)
teloti = init(teloti_fs)
pamoda = init(pamoda_fs)
tomute = init(tomute_fs)
vumali = init(vumali_fs)

futare = init(futare_fs)
geteso = init(geteso_fs)
bitada = init(bitada_fs)
duvola = init(duvola_fs)

futare_bloatless = futare.bloatless_boolf
geteso_bloatless = geteso.blightless_boolf
bitada_blightless = bitada.blightless_boolf
duvola_blightless = duvola.blightless_boolf


# other variables

letters_a_to_h = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

t10_filtrated_pairs_pretty_of_teloti_and_lenevu = {
    'disjoint': [('A', 'D'), ('A', 'E'), ('A', 'F'), ('A', 'G'), ('A', 'H'), ('C', 'F'), ('C', 'G'), ('C', 'H'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('F', 'G'), ('F', 'H'), ('G', 'H')],
    'crossing': [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'D'), ('C', 'E')],
    'subset': [('E', 'D'), ('F', 'B'), ('F', 'D'), ('G', 'B'), ('G', 'D'), ('H', 'B'), ('H', 'D')]
}

# examples dinado, doguva, kulika, part of kokabi, pamoda
t10_common_disjoint_pairs = [('A', 'D'), ('A', 'E'), ('A', 'F'), ('A', 'G'), ('A', 'H'), ('C', 'F'), ('C', 'G'), ('C', 'H'), ('E', 'F'), ('E', 'G'), ('E', 'H'), ('F', 'H')]

t10_all_spot_degrees = {0: 4, 1: 3, 2: 4, 3: 3, 4: 4, 5: 3, 6: 4, 7: 3, 8: 4, 10: 7, 12: 4, 14: 4, 24: 3, 26: 3, 28: 3, 30: 3, 42: 2, 74: 3, 106: 2, 138: 2, 202: 2}
