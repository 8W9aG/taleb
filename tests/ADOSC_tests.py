"""Tests for the ADOSC function."""
import taleb

import math

import numpy as np

from .data import create_dataset


def test_ADOSC():
    df = create_dataset()
    result = taleb.ADOSC(df["High"].to_numpy(), df["Low"].to_numpy(), df["Close"].to_numpy(), df["Volume"].to_numpy())
    expected = np.array([
               math.nan,        math.nan,        math.nan,        math.nan,        math.nan,
              math.nan,        math.nan,        math.nan,        math.nan, 0.81491221,
       0.92741194, 0.97056185, 1.04976455, 1.00480989, 1.00430227,
       1.03081088, 1.03989055, 1.0858146 , 1.1633781 , 1.22296966,
       1.21389177, 1.21530949, 1.22199365, 1.2166613 , 1.13574376,
       1.00001391, 1.00621472, 0.97231347, 0.92774079, 0.96969462,
       0.95626401, 1.00914914, 1.09185199, 1.18241214, 1.20933626,
       1.2680941 , 1.29532419, 1.31930473, 1.35289218, 1.29479521,
       1.20888617, 1.19852232, 1.11402105, 0.98799312, 1.00059415,
       1.03966655, 1.07672262, 1.14046705, 1.19539235, 1.20716139,
       1.10935336, 0.97636154, 0.9049183 , 0.89896198, 0.91499572,
       0.91118528, 0.97810387, 1.06543314, 1.10056501, 1.16326521,
       1.18658464, 1.2314838 , 1.13967357, 1.12428623, 1.14300084,
       1.06911784, 0.94755693, 0.91706366, 0.88955395, 0.92777756,
       0.8989114 , 0.84882696, 0.87126697, 0.92715058, 0.87392282,
       0.90481934, 0.95858792, 0.93425045, 0.90918498, 0.89167256,
       0.85498587, 0.78786589, 0.7152541 , 0.7331944 , 0.70591947,
       0.6516348 , 0.6403352 , 0.61574197, 0.59755099, 0.61097176,
       0.66152924, 0.75880467, 0.81494974, 0.80392311, 0.87939043,
       0.9579014 , 1.03459877, 0.98672408, 0.98047626, 0.96883867
    ])
    np.testing.assert_almost_equal(expected, result)