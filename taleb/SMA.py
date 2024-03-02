"""Function for computing Simple Moving Average."""
# pylint: disable=C0103,C0200

import math

import numpy as np


def SMA(
    values: np.ndarray,
    timeperiod: int = 30,
) -> np.ndarray:
    """Compute Simple Moving Average."""

    period_total = 0.0
    out = np.zeros(len(values))
    for i in range(len(values)):
        period_total += values[i]
        out[i] = math.nan
        if i >= timeperiod - 1:
            out[i] = period_total / float(timeperiod)
            period_total -= values[i - timeperiod + 1]

    return out
