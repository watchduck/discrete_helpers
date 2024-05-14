def __str__(self):

    if self.length <= 16:

        return f"Binv('{self.string}')"

    else:

        show_complement = self.weight > self.length / 2
        exposet_set = self.complement.exposet if show_complement else self.exposet
        exposet_list = sorted(exposet_set)
        maybe_tilda = '~' if show_complement else ''
        return f"{maybe_tilda}Binv(exposet={exposet_list}, length={self.length})"


def __hash__(self):
    return hash(self.__str__())

