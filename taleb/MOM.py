"""Function for computing Momentum."""
# pylint: disable=C0103

import numpy as np
from scipy.ndimage import shift


def MOM(values: np.ndarray, timeperiod: int = 10) -> np.ndarray:
    """Compute Momentum."""
    return values - shift(values, timeperiod, cval=np.NaN)
