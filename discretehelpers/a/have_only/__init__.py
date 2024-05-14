from discretehelpers.ex import ArgComboError


def have_only(check_args, all_args):

    for arg in check_args:
        if arg is None:
            return False

    number_of_check_args = len(check_args)
    number_of_all_args = len(all_args)
    number_of_expected_none_args = number_of_all_args - number_of_check_args

    number_of_none_args = all_args.count(None)
    if number_of_none_args < number_of_expected_none_args:
        raise ArgComboError

    return True
