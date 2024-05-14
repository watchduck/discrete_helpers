from discretehelpers.boolf import Boolf


def test():

    zhe_to_boolf = {
        321: Boolf('1110 0001', [1, 2, 3]),
        1234: Boolf('0101 1000 0110 1011'),
        111222333: ~Boolf(fullspots={2, 4, 9, 11, 16, 17, 19, 22, 23, 24, 25, 28, 29, 31}, arity=5),
        56289841393937: Boolf('1100 0001 1011 1110', [0, 2, 3, 5])
    }

    for zhe, boolf in zhe_to_boolf.items():
        assert Boolf(zhe=zhe) == boolf
        assert boolf.zhe == zhe
