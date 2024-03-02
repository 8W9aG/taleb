"""Function for computing Chaikin A/D Oscillator."""
# pylint: disable=C0103,C0200,too-many-arguments

import math

import numpy as np


def ADOSC(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    volume: np.ndarray,
    fastperiod: int = 3,
    slowperiod: int = 10,
) -> np.ndarray:
    """Compute Chaikin A/D Oscillator."""
    slowperiod = max(slowperiod, fastperiod)
    ad = 0.0
    fastk = 2.0 / (float(fastperiod) + 1.0)
    slowk = 2.0 / (float(slowperiod) + 1.0)
    fast_ema = 0.0
    slow_ema = 0.0
    adosc_ret = np.zeros(len(high))
    for i in range(len(high)):
        tmp = high[i] - low[i]
        if tmp > 0.0:
            ad += (((close[i] - low[i]) - (high[i] - close[i])) / tmp) * volume[i]
        adosc_ret[i] = math.nan
        if i == 0:
            fast_ema = ad
            slow_ema = ad
        else:
            fast_ema = (fastk * ad) + ((1.0 - fastk) * fast_ema)
            slow_ema = (slowk * ad) + ((1.0 - slowk) * slow_ema)
            if i > slowperiod - 2:
                adosc_ret[i] = fast_ema - slow_ema
    return adosc_ret
