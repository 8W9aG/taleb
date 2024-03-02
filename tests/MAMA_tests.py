"""Tests for the MAMA function."""
import taleb

import math

import numpy as np

from .data import create_dataset


"""
def test_MAMA():
    df = create_dataset()
    result = taleb.MAMA(df["Close"].to_numpy())
    expected_1 = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan, 0.46230024, 0.52547101, 0.51041065,
       0.48954773, 0.48472165, 0.4745318 , 0.45952687, 0.41015622,
       0.39975702, 0.42204491, 0.42601656, 0.47270064, 0.75702477,
       0.85254123, 0.81292464, 0.82202154, 0.81575803, 0.88864404,
       0.85188294, 0.83402588, 0.83190956, 0.44334752, 0.44564475,
       0.58813693, 0.60207458, 0.55868377, 0.30915179, 0.3043472 ,
       0.42018013, 0.40249603, 0.40258502, 0.63756394, 0.62831842,
       0.63655449, 0.63437174, 0.36376248, 0.36063191, 0.39087611,
       0.39704214, 0.42457895, 0.39701371, 0.40181148, 0.45393376,
       0.46882358, 0.45749225, 0.44945858, 0.4247281 , 0.41365675,
       0.47827159, 0.43854924, 0.42984555, 0.45334919, 0.30756824,
       0.29749347, 0.42771435, 0.43308084, 0.51066497, 0.53408692,
       0.45216828, 0.47320646, 0.40676916, 0.25942081, 0.25859657,
       0.2799946 , 0.48006355, 0.49078142, 0.47259094, 0.48673043
    ])
    expected_2 = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan, 0.44322192, 0.46378419, 0.46494985,
       0.4655648 , 0.46604372, 0.46816574, 0.46794977, 0.45350138,
       0.45215777, 0.45140495, 0.45077024, 0.45625284, 0.53144582,
       0.61171967, 0.6167498 , 0.62188159, 0.6267285 , 0.69220739,
       0.69619928, 0.73065593, 0.73318727, 0.66072733, 0.65535027,
       0.63854693, 0.63763512, 0.63096736, 0.55051347, 0.54435931,
       0.51331452, 0.51054405, 0.50784508, 0.54027479, 0.54247588,
       0.54482785, 0.54789962, 0.50186533, 0.4983345 , 0.49564804,
       0.49318289, 0.49146779, 0.46785427, 0.4662032 , 0.46313584,
       0.46327803, 0.46313339, 0.46279152, 0.45327566, 0.45228519,
       0.45878179, 0.45372365, 0.4531267 , 0.45313226, 0.41674126,
       0.41376006, 0.41724863, 0.41764444, 0.44089957, 0.44322925,
       0.44546401, 0.44615757, 0.43631047, 0.39208806, 0.38875077,
       0.38603186, 0.40953979, 0.41267592, 0.4141738 , 0.41598771
    ])
    expected = (expected_1, expected_2)
    for count, expected_arr in enumerate(expected):
        print(result[count])
        print(expected_arr)
        np.testing.assert_almost_equal(expected_arr, result[count])
"""
