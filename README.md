# taleb

<a href="https://pypi.org/project/taleb/">
    <img alt="PyPi" src="https://img.shields.io/pypi/v/taleb">
</a>

A pure python version of [ta-lib](https://ta-lib.org/).

## Dependencies :globe_with_meridians:

Python 3.11.6:

- [numpy 1.26.4](https://numpy.org/)
- [pandas 2.2.1](https://pandas.pydata.org/)
- [scipy 1.12.0](https://scipy.org/)

## Raison D'être :thought_balloon:

taleb is a pure python implementation of the [ta-lib](https://ta-lib.org/) C library that doesn't call out to any library other than python dependencies.
Thus it doesn't require ta-lib to be installed on a system before use, and is extremely portable.
In addition to this it uses vectorisation where applicable.
This library has the exact API as [ta-lib-python](https://github.com/TA-Lib/ta-lib-python) where implemented.

```python
import taleb
import numpy as np

close = np.random.random(100)
taleb.MOM(close)
```

It is designed to be a drop-in replacement where instead of importing `talib` you import `taleb`.

## Installation :inbox_tray:

This is a python package hosted on pypi, so to install simply run the following command:

`pip install taleb`

Note that upon running this package for the first time, you may notice a slight delay as it downloads the relevant R packages.

## Usage example :eyes:

To get familiar with the individual functions and charts check out the documents in the [ta-lib documentation](https://ta-lib.org/functions/). This library ports over 200 functions.

## License :memo:

The project is available under the [MIT License](LICENSE).
