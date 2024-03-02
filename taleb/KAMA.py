"""Function for computing Kaufman Adaptive Moving Average."""
# pylint: disable=C0103,C0200

import math

import numpy as np


def KAMA(
    values: np.ndarray,
    timeperiod: int = 30,
) -> np.ndarray:
    """Compute Kaufman Adaptive Moving Average."""
    const_max = 2.0 / (30.0 + 1.0)
    const_diff = 2.0 / (2.0 + 1.0) - const_max

    sum_roc1 = 0.0
    today = 0
    trailing_idx = today
    i = timeperiod
    while i > 0:
        i -= 1
        tmp_real = values[today]
        today += 1
        tmp_real -= values[today]
        sum_roc1 += abs(tmp_real)

    prev_kama = values[today - 1]
    tmp_real = values[today]
    tmp_real_2 = values[trailing_idx]
    trailing_idx += 1
    period_roc = tmp_real - tmp_real_2
    trailing_value = tmp_real_2
    if sum_roc1 <= period_roc or math.isclose(sum_roc1, 0.0):
        tmp_real = 1.0
    else:
        tmp_real = abs(period_roc / sum_roc1)
    tmp_real = (tmp_real * const_diff) + const_max
    tmp_real *= tmp_real
    prev_kama = ((values[today] - prev_kama) * tmp_real) + prev_kama
    today += 1

    out = np.zeros(len(values))
    out[:] = math.nan
    out[timeperiod] = prev_kama
    out_idx = timeperiod + 1
    while today < len(values):
        tmp_real = values[today]
        tmp_real_2 = values[trailing_idx]
        trailing_idx += 1
        period_roc = tmp_real - tmp_real_2
        sum_roc1 -= abs(trailing_value - tmp_real_2)
        sum_roc1 += abs(tmp_real - values[today - 1])
        trailing_value = tmp_real_2
        if sum_roc1 <= period_roc or math.isclose(sum_roc1, 0.0):
            tmp_real = 1.0
        else:
            tmp_real = abs(period_roc / sum_roc1)
        tmp_real = (tmp_real * const_diff) + const_max
        tmp_real *= tmp_real
        prev_kama = ((values[today] - prev_kama) * tmp_real) + prev_kama
        today += 1
        if out_idx < len(values):
            out[out_idx] = prev_kama
        out_idx += 1

    return out
