"""Function for computing All Moving Average."""
# pylint: disable=C0103,C0200,too-many-return-statements

import numpy as np

from .DEMA import DEMA
from .EMA import EMA
from .KAMA import KAMA
from .MAMA import MAMA
from .moving_average_type import MovingAverageType
from .SMA import SMA
from .TEMA import TEMA
from .TRIMA import TRIMA
from .WMA import WMA


def MA(
    values: np.ndarray,
    timeperiod: int = 30,
    mattype: int = MovingAverageType.Sma,
) -> np.ndarray:
    """Compute All Moving Average."""

    if mattype == MovingAverageType.Sma:
        return SMA(values, timeperiod=timeperiod)
    if mattype == MovingAverageType.Ema:
        return EMA(values, timeperiod=timeperiod)
    if mattype == MovingAverageType.Wma:
        return WMA(values, timeperiod=timeperiod)
    if mattype == MovingAverageType.Dema:
        return DEMA(values, timeperiod=timeperiod)
    if mattype == MovingAverageType.Tema:
        return TEMA(values, timeperiod=timeperiod)
    if mattype == MovingAverageType.Trima:
        return TRIMA(values, timeperiod=timeperiod)
    if mattype == MovingAverageType.Kama:
        return KAMA(values, timeperiod=timeperiod)
    if mattype == MovingAverageType.Mama:
        return MAMA(values)[0]

    raise ValueError(f"Could not interpret moving average type: {mattype}")
