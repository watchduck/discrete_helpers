def boolf(self):
    from discretehelpers.boolf import Boolf

    boolf_object = Boolf(True)
    for equality_block in self.equal_part.blocks:
        for i in range(len(equality_block) - 1):
            a, b = equality_block[i:i + 2]  # two consecutive elements
            boolf_object = boolf_object & Boolf('1001', [a, b])
    for a, b in self.comp_pairs:
        boolf_object = boolf_object & Boolf('0110', [a, b])
    return boolf_object
