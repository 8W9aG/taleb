"""Function for computing Triangular Moving Average."""
# pylint: disable=C0103,C0200

import math

import numpy as np

from .SMA import SMA


def TRIMA(
    values: np.ndarray,
    timeperiod: int = 30,
) -> np.ndarray:
    """Compute Triangular Moving Average."""

    out = np.zeros(len(values))
    out[:] = math.nan
    sma_period = int((timeperiod + (timeperiod % 2)) / 2)
    sma = SMA(values, timeperiod=sma_period)
    next_sma_period = sma_period + ((timeperiod + 1) % 2)
    out[sma_period - 1 :] = SMA(sma[sma_period - 1 :], timeperiod=next_sma_period)

    return out
