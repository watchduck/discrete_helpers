# library


``` 
pip install setuptools
pip install wheel
pip install twine
```

Run [setup.py](../setup.py):<br>
```
python setup.py bdist_wheel
```

The folders where created:
* `dist` with a compressed file
* `discretehelpers.egg-info` with metadata
* `build` with the whole project &nbsp; (can be deleted)

The library can now be installed with:

```
pip install ~/Code/discrete_helpers/dist/discretehelpers-0.0.1-py3-none-any.whl
```

## TL;DR:

Run this command from root folder:<br>
```
python setup.py bdist_wheel
```

Then delete the build folder.
