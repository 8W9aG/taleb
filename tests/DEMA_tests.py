"""Tests for the DEMA function."""
import taleb

import math

import numpy as np

from .data import create_dataset


def test_DEMA():
    df = create_dataset()
    result = taleb.DEMA(df["Close"].to_numpy())
    expected = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan, 0.53327934, 0.49352319,
       0.49789113, 0.44324402, 0.43603084, 0.48805865, 0.48275856,
       0.52049899, 0.53114824, 0.47689219, 0.45378652, 0.51588991,
       0.51575375, 0.56976944, 0.54639757, 0.54063161, 0.53702145,
       0.56441051, 0.52553383, 0.49715294, 0.48436605, 0.44826323,
       0.45805292, 0.44898458, 0.42406336, 0.48093753, 0.44028338,
       0.39658944, 0.41356638, 0.4261659 , 0.44428901, 0.50955432,
       0.49259678, 0.54001736, 0.51639652, 0.46648964, 0.43768034,
       0.46705281, 0.49286895, 0.50859315, 0.46138753, 0.49715392
    ])
    np.testing.assert_almost_equal(expected, result)
