"""Tests for the AD function."""
import taleb

import numpy as np

from .data import create_dataset


def test_AD():
    df = create_dataset()
    ad = taleb.AD(df["High"].to_numpy(), df["Low"].to_numpy(), df["Close"].to_numpy(), df["Volume"].to_numpy())
    expected = np.array([
        0.17957086,  0.33497229,  0.38634714,  0.52808707,  0.93156801,
        1.33525877,  1.50403518,  1.99510724,  2.15346408,  2.6458591 ,
        3.08684327,  3.34278961,  3.81353733,  3.87035193,  4.21364395,
        4.58455288,  4.87352386,  5.30329435,  5.79825286,  6.21820986,
        6.46248155,  6.82543503,  7.19185087,  7.5156392 ,  7.61580032,
        7.61775585,  8.09747216,  8.27044285,  8.45174843,  8.90597988,
        9.08688435,  9.54358096, 10.02383736, 10.51408046, 10.8200967 ,
       11.3156721 , 11.68801918, 12.09846911, 12.55014175, 12.71090804,
       12.88554579, 13.30882422, 13.3990087 , 13.42985712, 13.91378003,
       14.30626173, 14.66953528, 15.12986646, 15.54637943, 15.85429026,
       15.87666523, 15.90140223, 16.12681625, 16.45850005, 16.77339623,
       17.00223309, 17.47778645, 17.94566995, 18.24821335, 18.71454872,
       19.03958533, 19.489739  , 19.49531761, 19.89062013, 20.29044583,
       20.36075215, 20.37915826, 20.7103454 , 20.92511013, 21.3347694 ,
       21.45998182, 21.59651906, 21.97396107, 22.36967724, 22.39543981,
       22.8106711 , 23.19845378, 23.32671581, 23.54615835, 23.7831135 ,
       23.94509202, 24.02559377, 24.10878697, 24.4628871 , 24.56358389,
       24.62973399, 24.85019688, 24.97038488, 25.12075934, 25.35705618,
       25.67325919, 26.10298785, 26.3711767 , 26.49717785, 26.97823026,
       27.37920403, 27.79299635, 27.83952178, 28.1633601 , 28.41495382
    ])
    np.testing.assert_almost_equal(expected, ad)
