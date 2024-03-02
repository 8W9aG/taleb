"""An enum defining the moving average types."""

# pylint: disable=invalid-name
from enum import IntEnum


class MovingAverageType(IntEnum):
    """An integer enum for the different types of moving averages."""

    Sma = 0
    Ema = 1
    Wma = 2
    Dema = 3
    Tema = 4
    Trima = 5
    Kama = 6
    Mama = 7
    T3 = 8
