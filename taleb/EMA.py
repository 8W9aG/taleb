"""Function for computing Exponential Moving Average."""
# pylint: disable=C0103,C0200

import math

import numpy as np


def EMA(
    values: np.ndarray,
    timeperiod: int = 30,
) -> np.ndarray:
    """Compute Exponential Moving Average."""

    prev_ma = values[:timeperiod].sum() / float(timeperiod)
    k = 2.0 / float(timeperiod + 1)
    out = np.zeros(len(values))
    for i in range(len(values)):
        out[i] = math.nan
        if i == timeperiod - 1:
            out[i] = prev_ma
        elif i > timeperiod - 1:
            prev_ma = ((values[i] - prev_ma) * k) + prev_ma
            out[i] = prev_ma

    return out
