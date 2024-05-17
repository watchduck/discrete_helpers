from discretehelpers.boolf import Boolf
from discretehelpers.boolf.examples import medusa, bunese, darimi, kinide, putuki, futare


boolf_to_zhe = {
    medusa: 43009,
    bunese: 129,
    darimi: 1426146561,
    kinide: 249,
    putuki: 33825,
    futare: 57670775087675706393438255597061710309579425972925383989832448482994439618688
}


def test():
    for boolf, zhe in boolf_to_zhe.items():
        assert boolf.zhe == zhe
        assert Boolf(zhe=zhe) == boolf
