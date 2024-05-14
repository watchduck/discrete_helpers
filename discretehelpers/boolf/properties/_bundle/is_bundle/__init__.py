from functools import cached_property


@cached_property
def is_bundle(self):

    return len(self.bundles) == 1
