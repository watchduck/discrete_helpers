from discretehelpers.a import abbrev_testing as abbrev

from discretehelpers.boolf.examples import vinona, takate

from discretehelpers.ex import ArgTooSmallError


def test():

    assert vinona.ec_clan_factions(2) == {
        9: [9],
        11: [11, 13],
        14: [14]
    }
    assert vinona.ec_clan_factions(3) == {
        9: [9, 33, 65],
        11: [11, 13, 35, 49, 69, 81],
        14: [14, 50, 84]
    }

    assert takate.ec_clan_factions(3) == {
        24: [24, 36, 66],
        25: [25, 37, 67],
        26: [26, 28, 38, 52, 70, 82],
        27: [27, 29, 39, 53, 71, 83],
        30: [30, 54, 86],
        31: [31, 55, 87]
    }
    assert takate.ec_clan_factions(4) == {
        24: [24, 36, 66, 264, 288, 320, 516, 528, 1026, 1040, 4098, 4100],
        25: [25, 37, 67, 265, 289, 321, 517, 529, 1027, 1041, 4099, 4101],
        26: [26, 28, 38, 52, 70, 82, 266, 268, 290, 304, 324, 336, 518, 530, 772, 784, 1030, 1044, 1282, 1296, 4114, 4116, 4354, 4356],
        27: [27, 29, 39, 53, 71, 83, 267, 269, 291, 305, 325, 337, 519, 531, 773, 785, 1031, 1045, 1283, 1297, 4115, 4117, 4355, 4357],
        30: [30, 54, 86, 270, 306, 340, 774, 786, 1286, 1300, 4370, 4372],
        31: [31, 55, 87, 271, 307, 341, 775, 787, 1287, 1301, 4371, 4373]
    }


def test_raise():
    abbrev(ArgTooSmallError, [
        lambda: vinona.ec_clan_factions(1),
        lambda: takate.ec_clan_factions(2)
    ])
