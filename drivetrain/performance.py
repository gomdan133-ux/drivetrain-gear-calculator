"""Road speed and pulling force."""
import math


def road_speed(rpm: float, overall: float, tire_d_m: float) -> float:
    """Vehicle speed (m/s) with no slip: v = rpm/overall * pi * D / 60."""
    if rpm < 0 or overall <= 0 or tire_d_m <= 0:
        raise ValueError("invalid input")
    return rpm / overall * math.pi * tire_d_m / 60


def rpm_at_speed(speed_mps: float, overall: float, tire_d_m: float) -> float:
    """Engine RPM needed for a road speed (m/s)."""
    if speed_mps < 0 or overall <= 0 or tire_d_m <= 0:
        raise ValueError("invalid input")
    return speed_mps * 60 * overall / (math.pi * tire_d_m)


def tractive_force(engine_torque_nm: float, overall: float, tire_d_m: float,
                   driveline_eff: float = 0.90) -> float:
    """Force at the tire contact patch (N): F = T * ratio * eff / r."""
    if engine_torque_nm < 0 or overall <= 0 or tire_d_m <= 0 or not 0 < driveline_eff <= 1:
        raise ValueError("invalid input")
    return engine_torque_nm * overall * driveline_eff / (tire_d_m / 2)
