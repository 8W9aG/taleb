"""Function for computing Average Directional Movement Index Rating."""
# pylint: disable=C0103,C0200

import math

import numpy as np

from .ADX import ADX


def ADXR(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    timeperiod: int = 14,
) -> np.ndarray:
    """Compute Average Directional Movement Index Rating."""

    adx = ADX(high, low, close, timeperiod=timeperiod)

    out = np.zeros(len(adx))
    out[:] = math.nan
    for i in range(len(out)):
        if i < (timeperiod * 3) - 4:
            continue
        out[i] = (adx[i] + adx[i - timeperiod + 1]) / 2.0

    return out
