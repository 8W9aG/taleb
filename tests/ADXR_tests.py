"""Tests for the ADXR function."""
import taleb

import math

import numpy as np

from .data import create_dataset


def test_ADXR():
    df = create_dataset()
    result = taleb.ADXR(df["High"].to_numpy(), df["Low"].to_numpy(), df["Close"].to_numpy())
    expected = np.array([
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
       7.92102285, 7.83382031, 7.55048214, 7.40953303, 7.54608905,
       7.6377118 , 7.55277292, 7.64144432, 7.59647625, 7.46901022,
       7.32812776, 7.2789614 , 7.03943318, 7.17477165, 6.99738565,
       6.62175381, 6.34543356, 6.48668133, 6.70713011, 6.86176737,
       6.68112354, 6.59394095, 6.44114281, 6.54343824, 6.25783272,
       6.12945313, 6.09238435, 6.01001494, 5.82484593, 5.91746247,
       5.66590567, 5.88560148, 5.80997877, 5.43533878, 5.38028203,
       5.21406499, 5.32081522, 5.15302361, 5.06538904, 5.00070233,
       4.9932873 , 4.85085357, 5.01005888, 5.00888904, 5.17446018,
       5.20586965, 4.9501427 , 4.6841399 , 4.62065919, 4.94009776,
       4.86636786, 4.89318173, 4.91957171, 4.91515077, 4.82325551,
       4.83677576, 5.00746314, 5.00409879, 5.24520584, 5.17216012
    ])
    np.testing.assert_almost_equal(expected, result)
