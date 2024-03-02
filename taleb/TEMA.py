"""Function for computing Triple Exponential Moving Average."""
# pylint: disable=C0103,C0200

import math

import numpy as np

from .EMA import EMA


def TEMA(
    values: np.ndarray,
    timeperiod: int = 30,
) -> np.ndarray:
    """Compute Triple Exponential Moving Average."""

    ema = EMA(values, timeperiod=timeperiod)
    ema2 = np.zeros(len(values))
    ema2[:] = math.nan
    ema2[timeperiod - 1 :] = EMA(ema[timeperiod - 1 :], timeperiod=timeperiod)
    ema3 = np.zeros(len(values))
    ema3[:] = math.nan
    ema3[(timeperiod - 1) * 2 :] = EMA(
        ema2[(timeperiod - 1) * 2 :], timeperiod=timeperiod
    )

    return (3.0 * ema) - (3.0 * ema2) + ema3
