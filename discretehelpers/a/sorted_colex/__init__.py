def sorted_colex(unordered):
    unordered_reflected = [_[::-1] for _ in unordered]
    ordered_reflected = sorted(unordered_reflected)
    return [_[::-1] for _ in ordered_reflected]
