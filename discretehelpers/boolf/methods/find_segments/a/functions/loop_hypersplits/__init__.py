def loop_hypersplits(collection):

    """
    Loops through the potential cores of hypersplits.
    If there is exactly one, it must be the core, and will be added.
    Nothing is returned, because the argument is changed, using its `demand` method.

    The assumption behind this method is, that every hypersplit must have at least one core segment.
    But this demand may be too strict. There are good Euler diagrams that do not satisfy it.
    If this approach is used, it must be made sure that all cores are found - not just those that are easy to find.
    """

    from discretehelpers.boolf import Boolf

    valency = collection.valency
    atomvals = collection.boolf.atomvals
    spots = collection.get_spots()
    boolf = Boolf(fullspots=spots, atomvals=atomvals, skip_deflation=True)

    for dimension, list_of_pc_dicts in boolf.hypersplits_potential_cores.items():
        for pc_dict in list_of_pc_dicts:
            one_core_found = False
            for vector in pc_dict['vectors']:
                if collection.inquire(vector):
                    one_core_found = True
                    break
            if not one_core_found:
                if not pc_dict['free']:  # There is only one potential core, so it can be demanded.
                    unique_core_vector = pc_dict['vectors'][0]
                    collection.demand(unique_core_vector)
                else:
                    pass  # TO DO: Figure out which of the possible cores should be added.
