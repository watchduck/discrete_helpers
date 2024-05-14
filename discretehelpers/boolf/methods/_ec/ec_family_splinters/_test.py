from discretehelpers.boolf import Boolf
from discretehelpers.boolf.examples import vinona, takate


def test():

    assert vinona.ec_family_splinters() == {
        9: [9],
        11: [11, 13],
        14: [14]
    }

    assert takate.ec_family_splinters() == {
        24: [24],
        25: [25],
        26: [26, 28],
        27: [27, 29],
        30: [30],
        31: [31]
    }

    assert Boolf(zhe=178).ec_family_splinters() == Boolf(zhe=211).ec_family_splinters() == {
        146: [146],
        178: [178],
        155: [155, 211],
        185: [185, 227],
        222: [222],
        237: [237]
    }

    assert Boolf(zhe=26817).ec_family_splinters() == Boolf(zhe=31371).ec_family_splinters() == {
        26817: [26817],
        26793: [26793, 31873],
        27074: [27074],
        27051: [27051, 32131],
        28323: [28323, 28577, 31371, 31625],
        28365: [28365, 31473],
        28622: [28622, 31730],
        31997: [31997],
        32254: [32254]
    }
