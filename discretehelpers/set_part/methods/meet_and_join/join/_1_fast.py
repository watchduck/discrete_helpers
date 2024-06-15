def join(self, other):

    from discretehelpers.set_part import SetPart

    domain = self.non_singletons | other.non_singletons

    result_blocks = []
    result_dict = {}

    # We build the join-blocks one block at a time.
    # The one we are currently working on is called `current_block`.
    # The latest addition is called `new_elements`.
    current_block = set()
    new_elements = set()

    def new_block(e):
        """Begin building a new join-block"""
        nonlocal current_block
        nonlocal new_elements
        # It is important that current_block starts out empty.
        # This way we add blocks from both self and other.
        current_block = set([])
        new_elements = set([e])

    def join_blocks(part):
        """expand the current block with the given partition"""
        nonlocal current_block
        nonlocal new_elements

        part_dict = part.non_singleton_to_block_index

        # expand only new elements via the block_list
        added_elements = set()
        added_blocks = set()
        for e in new_elements:
            if e in part_dict:
                added_blocks.add(part_dict[e])
            else:  # `e` is a singleton in the current partition
                added_elements.add(e)
        for block_index in added_blocks:
            added_elements |= set(part.blocks[block_index])
        # grow current block
        new_elements = added_elements - current_block
        current_block |= added_elements
        return len(new_elements)

    def close_block():
        """add the current block to the join result"""
        join_block_index = len(result_blocks)
        for e in current_block:
            result_dict[e] = join_block_index
        result_blocks.append(current_block)

    for element in domain:
        if element in result_dict:
            continue
        new_block(element)
        while join_blocks(self) + join_blocks(other) > 0:
            pass
        close_block()

    return SetPart(result_blocks)
