def __str__(self):

    if self.valency <= 4:

        pretty_tt = self.root.pretty
        if self.is_root:
            atomvals_string = ''
        else:
            atomvals_string_raw = ', '.join([str(_) for _ in self.atomvals])
            atomvals_string = f', [{atomvals_string_raw}]'
        return f"Boolf('{pretty_tt}'{atomvals_string})"

    show_tilda = self.weight_fract > 0.5
    tilda_string = '~' if show_tilda else ''

    fullspots = sorted(self.complement.fullspots) if show_tilda else sorted(self.fullspots)
    fullspots_string_raw = ', '.join([str(_) for _ in fullspots])

    if self.is_root:
        arity_or_atomvals = f'arity={self.adicity}'
    else:
        atomvals_string_raw = ', '.join([str(_) for _ in self.atomvals])
        arity_or_atomvals = f'atomvals=[{atomvals_string_raw}]'
    return f'{tilda_string}Boolf(fullspots=[{fullspots_string_raw}], {arity_or_atomvals})'


def __repr__(self):
    return self.__str__()


def __hash__(self):
    return hash(self.__str__())


def __lt__(self, other):
    return str(self) < str(other)


def __gt__(self, other):
    return other < self


def __le__(self, other):
    return self == other or self < other


def __ge__(self, other):
    return other <= self
