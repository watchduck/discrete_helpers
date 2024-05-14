class BlightError(Exception):
    pass


class SpreadError(Exception):
    pass


class VFractERROR(Exception):
    """ `vfract` must be smaller or greater 1/2."""
