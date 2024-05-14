from discretehelpers.a import true_except, have

from .ex import UnknownBlockError, UnknownElementError, LabelContradictionError


def add_label_to_block(self, block, label):

    block_list = list(block)
    true_except(block_list in self.canonical_blocks_with_singletons, UnknownBlockError)
    block_tuple = tuple(block)

    if block_tuple in self.block_labels.keys():
        true_except(self.block_labels[block_tuple] == label, LabelContradictionError)

    if label in self.block_labels.values():
        try:
            if self.block_labels[block_tuple] == label:
                pass
            else:
                pass
        except KeyError:  # block not even found, thus label must be used for different block
            pass

    self.block_labels[block_tuple] = label


def add_label_to_element(self, element, label):
    true_except(self.element_in_domain(element), UnknownElementError)

    block_from_element = self.element_to_block(element)  # could be singleton
    block_from_label = self.get_block_from_label(label)  # could be None

    old_label = self.get_label_from_block(block_from_element)  # could be None
    if have(old_label):
        if label != old_label:
            print(f'###### The block {block_from_element} already has label {old_label}, and can not be assigned label {label}.')
            raise LabelContradictionError

    if have(block_from_label):
        self.merge_pair(block_from_element[0], block_from_label[0])  # merge blocks from element and label
    else:
        block = self.element_to_block(element)
        self.add_label_to_block(block, label)


def get_label_from_block(self, block):
    try:
        return self.block_labels[tuple(block)]
    except KeyError:
        return None


def get_label_from_element(self, element):
    block = self.element_to_block(element)
    return self.get_label_from_block(block)


def get_block_from_label(self, label):
    try:
        return list(self.block_labels.inverse[label])
    except KeyError:
        return None


def get_block_from_element(self, element):
    label = self.get_label_from_element(element)
    return self.get_block_from_label(label)


def merge_block_labels(self, element_a, element_b):

    block_a = self.element_to_block(element_a)
    block_b = self.element_to_block(element_b)

    if block_a == block_b:
        return  # nothing to do

    label_a = self.get_label_from_block(block_a)
    label_b = self.get_label_from_block(block_b)
    true_except(not have(label_a) or not have(label_b), LabelContradictionError)

    # remove entries from `block_labels` if present (second argument to avoid KeyError if not found)
    self.block_labels.pop(tuple(block_a), None)
    self.block_labels.pop(tuple(block_b), None)

    merged_block = sorted(block_a + block_b)

    if have(label_a) or have(label_b):
        label = label_a if have(label_a) else label_b
        self.block_labels[tuple(merged_block)] = label  # not using `add_label_to_block` to avoid verification
