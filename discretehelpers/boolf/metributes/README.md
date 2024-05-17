# metributes (Python properties)

Most metributes use `@cached_property`.

But there are some closely related metributes, that use dummy variables, getters and setters:<br>

* [_basics/fullspotlinks_by_weight](_basics/fullspotlinks_by_weight/__init__.py)
* [_basics/fullspots_by_weight](_basics/fullspots_by_weight/__init__.py)
* [_ec_reps/faction_luckyrep](_ec_reps/faction_luckyrep/__init__.py)
* [_fissions/fission_walsh_spectra](_fissions/fission_walsh_spectra/__init__.py)
* [_fissions/fission_walsh_spectra_zipped](_fissions/fission_walsh_spectra_zipped/__init__.py)
* [_fissions/fissions](_fissions/fissions/__init__.py)
* [_fissions/fissions_weight](_fissions/fissions_weight/__init__.py)
* [_layered](_layered/__init__.py)
* [prefect](prefect/__init__.py)
* [_splits/splits_eq_blocks_and_pref_side](_splits/splits_eq_blocks_and_pref_side/__init__.py)
* [_splits/splits_equal_and_onesided](_splits/splits_equal_and_onesided/__init__.py)


* [_basics_obsolete/spot_atoms](_basics_obsolete/spot_atoms/__init__.py)
* [_basics_obsolete/spotlinks_by_weight/](_basics_obsolete/spotlinks_by_weight/__init__.py)
* [_basics_obsolete/spots_by_weight](_basics_obsolete/spots_by_weight/__init__.py)

Their dummy variables are defined in `set_dummies` in the [init file](../__init__.py) of _Boolf_.<br>
This approach will probably be replaced.
