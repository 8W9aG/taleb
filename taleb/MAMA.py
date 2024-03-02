"""Function for computing MESA Adaptive Moving Average."""

# pylint: disable=C0103,C0200,too-many-locals,too-many-branches,too-many-statements
import math
from typing import Tuple

import numpy as np


def MAMA(
    values: np.ndarray,
    fastlimit: float = 0.5,
    slowlimit: float = 0.05,
) -> Tuple[np.ndarray, np.ndarray]:
    """Compute MESA Adaptive Moving Average."""
    rad_2_deg = 180.0 / (4.0 * math.atan(1.0))
    a = 0.0962
    b = 0.5769

    trailing_wma_idx = 0
    today = trailing_wma_idx
    tmp_real = values[today]
    today += 1
    period_wma_sub = tmp_real
    period_wma_sum = tmp_real
    tmp_real = values[today]
    today += 1
    period_wma_sub += tmp_real
    period_wma_sum += tmp_real * 2.0
    tmp_real = values[today]
    today += 1
    period_wma_sub += tmp_real
    period_wma_sum += tmp_real * 3.0
    trailing_wma_value = 0.0

    i = 8
    smoothed_value = 0.0
    while i > 0:
        i -= 1
        tmp_real = values[today]
        today += 1
        period_wma_sub += tmp_real
        period_wma_sub -= trailing_wma_value
        period_wma_sum += tmp_real * 4.0
        trailing_wma_value = values[trailing_wma_idx]
        trailing_wma_idx += 1
        smoothed_value = period_wma_sum * 0.1
        period_wma_sum -= period_wma_sub

    hilbert_idx = 0
    detrender_odd = [0.0, 0.0, 0.0]
    detrender_even = [0.0, 0.0, 0.0]
    detrender = 0.0
    prev_detrender_odd = 0.0
    prev_detrender_even = 0.0
    prev_detrender_input_odd = 0.0
    prev_detrender_input_even = 0.0
    Q1_odd = [0.0, 0.0, 0.0]
    Q1_even = [0.0, 0.0, 0.0]
    Q1 = 0.0
    prev_Q1_odd = 0.0
    prev_Q1_even = 0.0
    prev_Q1_input_odd = 0.0
    prev_Q1_input_even = 0.0
    jI_odd = [0.0, 0.0, 0.0]
    jI_even = [0.0, 0.0, 0.0]
    jI = 0.0
    prev_jI_odd = 0.0
    prev_jI_even = 0.0
    prev_jI_input_odd = 0.0
    prev_jI_input_even = 0.0
    jQ_odd = [0.0, 0.0, 0.0]
    jQ_even = [0.0, 0.0, 0.0]
    jQ = 0.0
    prev_jQ_odd = 0.0
    prev_jQ_even = 0.0
    prev_jQ_input_odd = 0.0
    prev_jQ_input_even = 0.0
    period = 0.0
    out_idx = 0
    prev_I2 = prev_Q2 = 0.0
    Re = Im = 0.0
    mama = fama = 0.0
    I1_for_odd_prev_3 = I1_for_even_prev_3 = 0.0
    I1_for_odd_prev_2 = I1_for_even_prev_2 = 0.0
    prev_phase = 0.0
    out_mama = np.zeros(len(values))
    out_mama[:] = math.nan
    out_fama = np.zeros(len(values))
    out_fama[:] = math.nan
    while today < len(values):
        adjusted_prev_period = (0.075 * period) + 0.54
        today_value = values[today]
        period_wma_sub += today_value
        period_wma_sub -= trailing_wma_value
        period_wma_sum += today_value * 4.0
        trailing_wma_value = values[trailing_wma_idx]
        trailing_wma_idx += 1
        smoothed_value = period_wma_sum * 0.1
        period_wma_sum -= period_wma_sub
        if today % 2 == 0:
            hilbert_tmp_real = a * smoothed_value
            detrender = -detrender_even[hilbert_idx]
            detrender_even[hilbert_idx] = hilbert_tmp_real
            detrender += hilbert_tmp_real
            detrender -= prev_detrender_even
            prev_detrender_even = b * prev_detrender_input_even
            detrender += prev_detrender_input_even
            prev_detrender_input_even = smoothed_value
            detrender *= adjusted_prev_period

            hilbert_tmp_real = a * detrender
            Q1 = -Q1_even[hilbert_idx]
            Q1_even[hilbert_idx] = hilbert_tmp_real
            Q1 += hilbert_tmp_real
            Q1 -= prev_Q1_even
            prev_Q1_even = b * prev_Q1_input_even
            Q1 += prev_Q1_input_even
            prev_Q1_input_even = detrender
            Q1 *= adjusted_prev_period

            hilbert_tmp_real = a * I1_for_even_prev_3
            jI = -jI_even[hilbert_idx]
            jI_even[hilbert_idx] = hilbert_tmp_real
            jI += hilbert_tmp_real
            jI -= prev_jI_even
            prev_jI_even = b * prev_jI_input_even
            jI += prev_jI_input_even
            prev_jI_input_even = I1_for_even_prev_3
            jI *= adjusted_prev_period

            hilbert_tmp_real = a * Q1
            jQ = -jQ_even[hilbert_idx]
            jQ_even[hilbert_idx] = hilbert_tmp_real
            jQ += hilbert_tmp_real
            jQ -= prev_jQ_even
            prev_jQ_even = b * prev_jQ_input_even
            jQ += prev_jQ_input_even
            prev_jQ_input_even = Q1
            jQ *= adjusted_prev_period

            hilbert_idx += 1
            if hilbert_idx == 3:
                hilbert_idx = 0

            Q2 = (0.2 * (Q1 + jI)) + (0.8 * prev_Q2)
            I2 = (0.2 * (I1_for_even_prev_3 - jQ)) + (0.8 * prev_I2)
            I1_for_odd_prev_3 = I1_for_odd_prev_2
            I1_for_odd_prev_2 = detrender
            tmp_real_2 = 0.0
            if I1_for_even_prev_3 != 0.0:
                tmp_real_2 = math.atan(Q1 / I1_for_even_prev_3) * rad_2_deg
        else:
            hilbert_tmp_real = a * smoothed_value
            detrender = -detrender_odd[hilbert_idx]
            detrender_odd[hilbert_idx] = hilbert_tmp_real
            detrender += hilbert_tmp_real
            detrender -= prev_detrender_odd
            prev_detrender_odd = b * prev_detrender_input_odd
            detrender += prev_detrender_input_odd
            prev_detrender_input_odd = smoothed_value
            detrender *= adjusted_prev_period

            hilbert_tmp_real = a * detrender
            Q1 = -Q1_odd[hilbert_idx]
            Q1_odd[hilbert_idx] = hilbert_tmp_real
            Q1 += hilbert_tmp_real
            Q1 -= prev_Q1_odd
            prev_Q1_odd = b * prev_Q1_input_odd
            Q1 += prev_Q1_input_odd
            prev_Q1_input_odd = detrender
            Q1 *= adjusted_prev_period

            hilbert_tmp_real = a * I1_for_odd_prev_3
            jI = -jI_odd[hilbert_idx]
            jI_odd[hilbert_idx] = hilbert_tmp_real
            jI += hilbert_tmp_real
            jI -= prev_jI_odd
            prev_jI_odd = b * prev_jI_input_odd
            jI += prev_jI_input_odd
            prev_jI_input_odd = I1_for_odd_prev_3
            jI *= adjusted_prev_period

            hilbert_tmp_real = a * Q1
            jQ = -jQ_odd[hilbert_idx]
            jQ_odd[hilbert_idx] = hilbert_tmp_real
            jQ += hilbert_tmp_real
            jQ -= prev_jQ_odd
            prev_jQ_odd = b * prev_jQ_input_odd
            jQ += prev_jQ_input_odd
            prev_jQ_input_odd = Q1
            jQ *= adjusted_prev_period

            Q2 = (0.2 * (Q1 + jI)) + (0.8 * prev_Q2)
            I2 = (0.2 * (I1_for_odd_prev_3 - jQ)) + (0.8 * prev_I2)
            I1_for_even_prev_3 = I1_for_even_prev_2
            I1_for_even_prev_2 = detrender
            tmp_real_2 = 0.0
            if I1_for_odd_prev_3 != 0.0:
                tmp_real_2 = math.atan(Q1 / I1_for_odd_prev_3) * rad_2_deg

        tmp_real = prev_phase - tmp_real_2
        prev_phase = tmp_real_2
        tmp_real = max(tmp_real, 1.0)
        if tmp_real > 1.0:
            tmp_real = fastlimit / tmp_real
            tmp_real = max(tmp_real, slowlimit)
        else:
            tmp_real = fastlimit

        mama = (tmp_real * today_value) + ((1.0 - tmp_real) * mama)
        tmp_real *= 0.5
        fama = (tmp_real * mama) + ((1.0 - tmp_real) * fama)
        if out_idx >= 32:
            out_mama[out_idx] = mama
            out_fama[out_idx] = fama
        out_idx += 1

        Re = (0.2 * ((I2 * prev_I2) + (Q2 * prev_Q2))) + (0.8 * Re)
        Im = (0.2 * ((I2 * prev_Q2) - (Q2 * prev_I2))) + (0.8 * Im)
        prev_Q2 = Q2
        prev_I2 = I2
        tmp_real = period
        if Im != 0.0 and Re != 0.0:
            period = 360.0 / (math.atan(Im / Re) * rad_2_deg)
        tmp_real_2 = 1.5 * tmp_real
        period = min(period, tmp_real_2)
        if period < 6.0:
            period = 6.0
        elif period > 50.0:
            period = 50.0
        period = (0.2 * period) + (0.8 * tmp_real)
        today += 1

    return (out_mama, out_fama)
