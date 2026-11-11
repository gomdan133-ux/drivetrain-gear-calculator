"""Ratios, shifts and tire size effects."""


def overall_ratio(gear_ratio: float, final_drive: float) -> float:
    """Total reduction from engine to wheel."""
    if gear_ratio <= 0 or final_drive <= 0:
        raise ValueError("ratios must be > 0")
    return gear_ratio * final_drive


def rpm_after_shift(rpm_before: float, ratio_from: float, ratio_to: float) -> float:
    """Engine RPM right after a shift at the same road speed.

    rpm_after = rpm_before * ratio_to / ratio_from
    """
    if min(rpm_before, ratio_from, ratio_to) <= 0:
        raise ValueError("inputs must be > 0")
    return rpm_before * ratio_to / ratio_from


def tire_diameter_from_size(width_mm: float, aspect_pct: float, rim_in: float) -> float:
    """Overall tire diameter (m) from a size like 265/70R17.

    D = rim + 2 * sidewall, sidewall = width * aspect / 100.
    """
    if min(width_mm, aspect_pct, rim_in) <= 0:
        raise ValueError("inputs must be > 0")
    sidewall_m = width_mm * aspect_pct / 100 / 1000
    return rim_in * 0.0254 + 2 * sidewall_m


def effective_final_drive(final_drive: float, old_tire_d: float, new_tire_d: float) -> float:
    """Final drive the vehicle 'feels like' after a tire size change."""
    if min(final_drive, old_tire_d, new_tire_d) <= 0:
        raise ValueError("inputs must be > 0")
    return final_drive * old_tire_d / new_tire_d


def speedometer_error(indicated_speed: float, old_tire_d: float, new_tire_d: float) -> dict:
    """Actual speed when the speedometer is still calibrated for the old tire."""
    if min(old_tire_d, new_tire_d) <= 0 or indicated_speed < 0:
        raise ValueError("invalid input")
    actual = indicated_speed * new_tire_d / old_tire_d
    return {"actual": actual, "error_pct": (actual - indicated_speed) / indicated_speed * 100
            if indicated_speed else 0.0}
