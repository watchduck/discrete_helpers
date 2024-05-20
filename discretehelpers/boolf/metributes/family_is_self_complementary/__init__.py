from functools import cached_property


@cached_property
def family_is_self_complementary(self):

    if self.root.weight == self.root.length / 2:
        return self.family_minrep == self.complement.family_minrep
    else:
        return False
