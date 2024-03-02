"""Function for computing Weighted Moving Average."""
# pylint: disable=C0103,C0200

import math

import numpy as np


def WMA(
    values: np.ndarray,
    timeperiod: int = 30,
) -> np.ndarray:
    """Compute Weighted Moving Average."""

    divider = (float(timeperiod) * float(timeperiod + 1)) / 2.0
    period_sum = 0.0
    period_sub = 0.0
    out = np.zeros(len(values))
    for i in range(len(values)):
        out[i] = math.nan
        period_sub += values[i]
        if i < timeperiod - 1:
            period_sum += values[i] * float(i + 1)
        else:
            if i >= timeperiod:
                period_sub -= values[i - timeperiod]
            period_sum += values[i] * float(timeperiod)
            out[i] = period_sum / divider
            period_sum -= period_sub

    return out
