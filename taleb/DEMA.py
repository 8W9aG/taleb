"""Function for computing Double Exponential Moving Average."""
# pylint: disable=C0103,C0200

import math

import numpy as np

from .EMA import EMA


def DEMA(
    values: np.ndarray,
    timeperiod: int = 30,
) -> np.ndarray:
    """Compute Double Exponential Moving Average."""

    ema = EMA(values, timeperiod=timeperiod)
    ema2 = np.zeros(len(values))
    ema2[:] = math.nan
    ema2[timeperiod - 1 :] = EMA(ema[timeperiod - 1 :], timeperiod=timeperiod)

    return (2.0 * ema) - ema2
