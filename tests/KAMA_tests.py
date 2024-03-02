"""Tests for the KAMA function."""
import taleb

import math

import numpy as np

from .data import create_dataset


def test_KAMA():
    df = create_dataset()
    result = taleb.KAMA(df["Close"].to_numpy())
    expected = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
       0.38820729, 0.38814328, 0.3938335 , 0.39490772, 0.39413232,
       0.39222397, 0.39222956, 0.39269693, 0.39137413, 0.39103977,
       0.38874858, 0.39319683, 0.39403553, 0.39464223, 0.40373351,
       0.40809099, 0.40506378, 0.4132641 , 0.41614805, 0.42260666,
       0.41978848, 0.42236237, 0.42603932, 0.42061608, 0.42115917,
       0.42282901, 0.4249009 , 0.42412865, 0.42135398, 0.42020423,
       0.42099025, 0.41867549, 0.41853818, 0.42143668, 0.42162096,
       0.42545215, 0.42648319, 0.42415287, 0.4235314 , 0.4283826 ,
       0.42892737, 0.43143862, 0.43112685, 0.43139449, 0.43201745,
       0.43377921, 0.43273544, 0.43129216, 0.43108585, 0.42845822,
       0.4293355 , 0.42908543, 0.42753611, 0.43402022, 0.43208582,
       0.42863045, 0.42951983, 0.43013614, 0.4316699 , 0.43860231,
       0.43822185, 0.44381586, 0.44333283, 0.43926155, 0.43807683,
       0.439334  , 0.44049004, 0.44225437, 0.44044584, 0.44236714
    ])
    np.testing.assert_almost_equal(expected, result)
