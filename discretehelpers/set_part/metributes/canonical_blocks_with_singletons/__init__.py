from functools import cached_property


@cached_property
def canonical_blocks_with_singletons(self):

    result = self.blocks_with_singletons()

    return result
