from discretehelpers.boolf.examples import takate


def test():

    faction_reps, family_reps, faction_dict, family_dict, splinter_dict = takate.ec_clan_partitioned()

    assert faction_reps == [24, 25, 26, 27, 30, 31]
    assert family_reps == [24, 36, 66]

    assert faction_dict == {
        24: [24, 36, 66],
        25: [25, 37, 67],
        26: [26, 28, 38, 52, 70, 82],
        27: [27, 29, 39, 53, 71, 83],
        30: [30, 54, 86],
        31: [31, 55, 87]
    }

    assert family_dict == {
        24: [24, 25, 26, 27, 28, 29, 30, 31],
        36: [36, 37, 38, 39, 52, 53, 54, 55],
        66: [66, 67, 70, 71, 82, 83, 86, 87]
    }

    assert splinter_dict == {
        (24, 24): [24],
        (24, 36): [36],
        (24, 66): [66],

        (25, 24): [25],
        (25, 36): [37],
        (25, 66): [67],

        (26, 24): [26, 28],
        (26, 36): [38, 52],
        (26, 66): [70, 82],

        (27, 24): [27, 29],
        (27, 36): [39, 53],
        (27, 66): [71, 83],

        (30, 24): [30],
        (30, 36): [54],
        (30, 66): [86],

        (31, 24): [31],
        (31, 36): [55],
        (31, 66): [87]
    }