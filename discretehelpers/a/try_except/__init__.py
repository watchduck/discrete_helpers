def try_except(attempt=None, do_raise=None, if_raised=None):
    if if_raised is not None:
        try:
            attempt()
        except if_raised:
            raise do_raise
    else:
        try:
            attempt()
        except:
            raise do_raise
