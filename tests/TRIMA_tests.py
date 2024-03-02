"""Tests for the TRIMA function."""
import taleb

import math

import numpy as np

from .data import create_dataset


def test_TRIMA():
    df = create_dataset()
    result = taleb.TRIMA(df["Close"].to_numpy())
    expected = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan, 0.51389253,
       0.51179229, 0.51085944, 0.51295546, 0.51888197, 0.52784019,
       0.53411148, 0.5378638 , 0.5409978 , 0.54282521, 0.53952339,
       0.53486353, 0.53180473, 0.52477763, 0.51750494, 0.51346506,
       0.51182774, 0.51044578, 0.50959776, 0.50537381, 0.50205199,
       0.49881347, 0.50039656, 0.50387406, 0.50559306, 0.51148417,
       0.52195811, 0.53405463, 0.54530805, 0.55659071, 0.56421325,
       0.56740707, 0.56754206, 0.56652406, 0.56631547, 0.5635361 ,
       0.56034987, 0.55603155, 0.54703954, 0.53771006, 0.53086337,
       0.52257944, 0.51243065, 0.50229388, 0.49461397, 0.49007055,
       0.48987717, 0.49213271, 0.49391431, 0.49618775, 0.49668976,
       0.49826979, 0.49632676, 0.49597853, 0.50103578, 0.50171763,
       0.4987147 , 0.49498922, 0.49161669, 0.48854007, 0.48562885,
       0.47990731, 0.47591502, 0.47137195, 0.46607693, 0.46291599,
       0.46139265, 0.46208372, 0.46510948, 0.46420079, 0.46327053
    ])
    np.testing.assert_almost_equal(expected, result)
