def boolfs_to_swan(boolfs, verophile, print_list):

    from discretehelpers.boolf import Boolf

    list_to_be_sorted = []

    for boolf in boolfs:

        layered_weight = boolf.layered_weight
        layered_tt = boolf.layered_tt
        tt = boolf.tt().pretty

        if verophile:
            list_to_be_sorted.append([layered_weight, layered_tt, tt])
        else:  # falsophobe
            layered_weight_reflected = layered_weight[::-1]
            layered_tt_reflected = [_[::-1] for _ in layered_tt[::-1]]
            list_to_be_sorted.append([layered_weight_reflected, layered_tt_reflected, tt, layered_weight, layered_tt])

    list_to_be_sorted = sorted(list_to_be_sorted)

    if print_list:
        for row in list_to_be_sorted:
            if verophile:
                print(row[0], '   ', row[1], '   ', row[2])
            else:
                print(row[3], '   ', row[4], '   ', row[2])

    repr_index = -1 if verophile else 0

    repr_tt = list_to_be_sorted[repr_index][2]

    return Boolf(repr_tt)
