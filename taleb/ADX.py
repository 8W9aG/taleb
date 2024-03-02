"""Function for computing Average Directional Movement Index."""
# pylint: disable=C0103,C0200,too-many-locals,too-many-branches,too-many-statements

import math

import numpy as np


def _true_range(th: float, tl: float, yc: float) -> float:
    out = th - tl
    tmp = abs(th - yc)
    out = max(tmp, out)
    tmp = abs(tl - yc)
    out = max(tmp, out)
    return out


def ADX(
    high: np.ndarray,
    low: np.ndarray,
    close: np.ndarray,
    timeperiod: int = 14,
) -> np.ndarray:
    """Compute Average Directional Movement Index."""

    prev_minus_dm = 0.0
    prev_plus_dm = 0.0
    prev_tr = 0.0
    today = 0
    prev_high = high[today]
    prev_low = low[today]
    prev_close = close[today]
    i = timeperiod - 1
    while i > 0:
        i -= 1
        today += 1
        temp_real = high[today]
        diff_p = temp_real - prev_high
        prev_high = temp_real

        temp_real = low[today]
        diff_m = prev_low - temp_real
        prev_low = temp_real

        if diff_m > 0.0 and diff_p < diff_m:
            prev_minus_dm += diff_m
        elif diff_p > 0.0 and diff_p > diff_m:
            prev_plus_dm += diff_p

        temp_real = _true_range(prev_high, prev_low, prev_close)
        prev_tr += temp_real
        prev_close = close[today]

    sum_dx = 0.0
    i = timeperiod
    while i > 0:
        i -= 1
        today += 1
        temp_real = high[today]
        diff_p = temp_real - prev_high
        prev_high = temp_real

        temp_real = low[today]
        diff_m = prev_low - temp_real
        prev_low = temp_real

        prev_minus_dm -= prev_minus_dm / float(timeperiod)
        prev_plus_dm -= prev_plus_dm / float(timeperiod)

        if diff_m > 0.0 and diff_p < diff_m:
            prev_minus_dm += diff_m
        elif diff_p > 0.0 and diff_p > diff_m:
            prev_plus_dm += diff_p

        temp_real = _true_range(prev_high, prev_low, prev_close)
        prev_tr = prev_tr - (prev_tr / float(timeperiod)) + temp_real
        prev_close = close[today]

        if not math.isclose(prev_tr, 0.0):
            minus_di = 100.0 * (prev_minus_dm / prev_tr)
            plus_di = 100.0 * (prev_plus_dm / prev_tr)
            temp_real = minus_di + plus_di
            if not math.isclose(temp_real, 0.0):
                sum_dx += 100.0 * (abs(minus_di - plus_di) / temp_real)

    prev_adx = sum_dx / float(timeperiod)

    out = np.zeros(len(high))
    out[:] = math.nan
    while today < len(high) - 1:
        out[today] = prev_adx
        today += 1
        temp_real = high[today]
        diff_p = temp_real - prev_high
        prev_high = temp_real

        temp_real = low[today]
        diff_m = prev_low - temp_real
        prev_low = temp_real

        prev_minus_dm -= prev_minus_dm / float(timeperiod)
        prev_plus_dm -= prev_plus_dm / float(timeperiod)
        if diff_m > 0.0 and diff_p < diff_m:
            prev_minus_dm += diff_m
        elif diff_p > 0.0 and diff_p > diff_m:
            prev_plus_dm += diff_p

        temp_real = _true_range(prev_high, prev_low, prev_close)
        prev_tr = prev_tr - (prev_tr / float(timeperiod)) + temp_real
        prev_close = close[today]

        if not math.isclose(prev_tr, 0.0):
            minus_di = 100.0 * (prev_minus_dm / prev_tr)
            plus_di = 100.0 * (prev_plus_dm / prev_tr)
            temp_real = minus_di + plus_di
            if not math.isclose(temp_real, 0.0):
                temp_real = 100.0 * (abs(minus_di - plus_di) / temp_real)
                prev_adx = ((prev_adx * float(timeperiod - 1)) + temp_real) / float(
                    timeperiod
                )

    out[today] = prev_adx

    return out
