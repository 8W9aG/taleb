"""Function for computing Chaikin A/D Line."""
# pylint: disable=C0103,C0200

import numpy as np


def AD(
    high: np.ndarray, low: np.ndarray, close: np.ndarray, volume: np.ndarray
) -> np.ndarray:
    """Compute Chaikin A/D Line."""
    ad = 0.0
    ad_ret = np.zeros(len(high))
    for i in range(len(high)):
        tmp = high[i] - low[i]
        if tmp > 0.0:
            ad += (((close[i] - low[i]) - (high[i] - close[i])) / tmp) * volume[i]
        ad_ret[i] = ad
    return ad_ret
