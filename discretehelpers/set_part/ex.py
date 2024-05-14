class NotInDomainError(ValueError):
    """Some new element can not be added, because it is not in the domain."""


class DomainsNotEqualError(ValueError):
    """Operations involving two SetPart objects require them to have the same domain. This includes equality."""


class DomainNotSetLikeError(TypeError):
    """The domain must be of type set, list or tuple."""


class DomainNotFiniteError(ValueError):
    """This works only when the domain is a finite set, not N or Z."""
