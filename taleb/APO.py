"""Function for computing Absolute Price Oscillator."""
# pylint: disable=C0103,C0200

import numpy as np

from .MA import MA
from .moving_average_type import MovingAverageType


def APO(
    values: np.ndarray,
    fastperiod: int = 12,
    slowperiod: int = 26,
    mattype: int = MovingAverageType.Sma,
) -> np.ndarray:
    """Compute Absolute Price Oscillator."""

    fast_ma = MA(values, timeperiod=fastperiod, mattype=mattype)
    slow_ma = MA(values, timeperiod=slowperiod, mattype=mattype)

    return fast_ma - slow_ma
