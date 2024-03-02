"""Tests for the SMA function."""
import taleb

import math

import numpy as np

from .data import create_dataset


def test_SMA():
    df = create_dataset()
    result = taleb.SMA(df["Close"].to_numpy())
    expected = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan, 0.54676117,
       0.52002969, 0.52152287, 0.53884847, 0.53329584, 0.5316658 ,
       0.52310603, 0.53388904, 0.52532813, 0.51822129, 0.49776996,
       0.47422839, 0.49195046, 0.48002712, 0.47753085, 0.5046856 ,
       0.51686066, 0.50151129, 0.53150677, 0.55246897, 0.57838707,
       0.55592797, 0.56578933, 0.58678104, 0.55369939, 0.53893559,
       0.54428264, 0.54653017, 0.52576102, 0.51210682, 0.50619213,
       0.5171376 , 0.50688489, 0.4865831 , 0.49604647, 0.50365946,
       0.52698905, 0.53404619, 0.52167323, 0.52589716, 0.54605483,
       0.55645565, 0.55986444, 0.55546346, 0.55458293, 0.53673983,
       0.53019558, 0.53626184, 0.51299371, 0.50310192, 0.47782762,
       0.49080977, 0.47689837, 0.45932423, 0.48749533, 0.4765785 ,
       0.45575995, 0.44546147, 0.45179012, 0.4694111 , 0.49494589,
       0.48942045, 0.51630157, 0.5141701 , 0.48882109, 0.4818305 ,
       0.47828108, 0.48079415, 0.49831861, 0.49251262, 0.48550812
    ])
    np.testing.assert_almost_equal(expected, result)
