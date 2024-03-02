"""Tests for the EMA function."""
import taleb

import math

import numpy as np

from .data import create_dataset


def test_EMA():
    df = create_dataset()
    result = taleb.EMA(df["Close"].to_numpy())
    expected = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan, 0.54676117,
       0.52488297, 0.51515371, 0.54729408, 0.54996168, 0.52894892,
       0.500833  , 0.49387771, 0.49197218, 0.4714858 , 0.46434385,
       0.44742955, 0.47311247, 0.4749425 , 0.47780974, 0.51416711,
       0.54216005, 0.51106646, 0.54227911, 0.55224507, 0.57865055,
       0.55121646, 0.56831016, 0.58272238, 0.54866193, 0.54483162,
       0.55681856, 0.57682316, 0.56187873, 0.52947493, 0.50906107,
       0.51079991, 0.48213528, 0.47711209, 0.50262375, 0.49939987,
       0.51834438, 0.52391831, 0.49612701, 0.48354793, 0.51464263,
       0.51461386, 0.54255996, 0.53139148, 0.5289126 , 0.52743799,
       0.54190845, 0.52257223, 0.50800749, 0.50103911, 0.48183022,
       0.48576933, 0.48016014, 0.46624499, 0.49422392, 0.4727764 ,
       0.4491181 , 0.45613856, 0.46122924, 0.46942407, 0.50230664,
       0.49378684, 0.5182478 , 0.50676935, 0.48130504, 0.46592639,
       0.48016063, 0.49306204, 0.50117977, 0.47703731, 0.49499496
    ])
    np.testing.assert_almost_equal(expected, result)
