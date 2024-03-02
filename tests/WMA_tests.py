"""Tests for the WMA function."""
import taleb

import math

import numpy as np

from .data import create_dataset


def test_WMA():
    df = create_dataset()
    result = taleb.WMA(df["Close"].to_numpy())
    expected = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan, 0.56011952,
       0.53824131, 0.52882517, 0.56055463, 0.5637671 , 0.54382956,
       0.51553835, 0.5071461 , 0.50265919, 0.48002082, 0.46986367,
       0.45079285, 0.47474681, 0.47536149, 0.47790069, 0.51427605,
       0.5428807 , 0.51341933, 0.54524845, 0.55590939, 0.58230043,
       0.55488334, 0.57167307, 0.58624792, 0.55192562, 0.54777032,
       0.56013764, 0.58095101, 0.56796097, 0.53788734, 0.51859401,
       0.52051794, 0.49144442, 0.48482448, 0.50972511, 0.50692557,
       0.52559527, 0.53061148, 0.50216677, 0.48793954, 0.51630204,
       0.51424667, 0.5394933 , 0.5272084 , 0.5231765 , 0.52004573,
       0.53391607, 0.51533552, 0.49988759, 0.49259752, 0.47325554,
       0.47745288, 0.4715185 , 0.45781379, 0.48623922, 0.4652258 ,
       0.4413222 , 0.44791416, 0.45369368, 0.46249749, 0.4953809 ,
       0.48733598, 0.51207864, 0.50072576, 0.47478398, 0.45892042,
       0.47212859, 0.48515126, 0.49406047, 0.4701026 , 0.48706184
    ])
    np.testing.assert_almost_equal(expected, result)
