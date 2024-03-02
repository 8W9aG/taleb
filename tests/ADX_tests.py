"""Tests for the ADX function."""
import taleb

import math

import numpy as np

from .data import create_dataset


def test_ADX():
    df = create_dataset()
    result = taleb.ADX(df["High"].to_numpy(), df["Low"].to_numpy(), df["Close"].to_numpy())
    expected = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan, 8.40629089, 8.19845379, 8.12261116,
       8.32808023, 8.20828661, 8.20916964, 7.73683938, 7.84183466,
       8.12802657, 7.85950476, 7.48462988, 7.61413411, 7.38017752,
       7.43575481, 7.46918683, 6.97835311, 6.49098583, 6.8838915 ,
       7.06625395, 7.36870647, 7.44105398, 7.06492592, 7.07851568,
       7.17162564, 6.94378869, 6.69868885, 6.91378849, 6.52558447,
       6.26515451, 6.1998813 , 6.08947116, 6.34800626, 6.35482827,
       5.92119311, 6.12295598, 5.80376993, 5.91525084, 5.57187675,
       5.56021741, 5.27098022, 5.49444541, 5.38453736, 5.63504365,
       5.24234018, 5.42319669, 5.26512927, 4.94948444, 4.63760809,
       4.62436004, 4.72637959, 4.73417046, 4.57056067, 4.73042444,
       4.49212919, 4.31716978, 4.3850741 , 4.7754379 , 4.92572367,
       5.14661002, 4.95080096, 4.7306717 , 4.61695834, 5.15381594,
       4.99856526, 5.21580279, 5.10871898, 5.33817236, 5.32934124,
       5.28847742, 5.23948837, 5.08247391, 5.34380166, 5.39351927
    ])
    np.testing.assert_almost_equal(expected, result)
