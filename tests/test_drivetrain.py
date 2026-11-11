import math

import pytest

from drivetrain import (effective_final_drive, overall_ratio, road_speed,
                        rpm_after_shift, rpm_at_speed, speedometer_error,
                        tire_diameter_from_size, tractive_force)


def test_overall_ratio():
    assert overall_ratio(3.5, 3.73) == pytest.approx(13.055)


def test_shift_drop():
    # 6000 rpm in a 3.5 gear, shift to 2.1 -> 3600 rpm
    assert rpm_after_shift(6000, 3.5, 2.1) == pytest.approx(3600)


def test_tire_size_265_70r17():
    # 17 in rim (0.4318 m) + 2 * 185.5 mm sidewall = 0.8028 m (31.6 in)
    d = tire_diameter_from_size(265, 70, 17)
    assert d == pytest.approx(0.8028, rel=1e-4)
    assert d / 0.0254 == pytest.approx(31.6, rel=1e-3)


def test_bigger_tires_effective_ratio_and_speedo():
    assert effective_final_drive(3.73, 30.5, 33) == pytest.approx(3.4474, rel=1e-4)
    e = speedometer_error(60, 30.5, 33)
    assert e["actual"] == pytest.approx(64.918, rel=1e-4)
    assert e["error_pct"] == pytest.approx(8.197, rel=1e-3)


def test_speed_and_rpm_round_trip():
    v = road_speed(2000, 0.7 * 3.73, 0.8)
    assert rpm_at_speed(v, 0.7 * 3.73, 0.8) == pytest.approx(2000)
    assert v == pytest.approx(2000 / 2.611 * math.pi * 0.8 / 60)


def test_tractive_force():
    # 400 N*m, overall 13.0, 0.7 m tire, 90% -> 400*13*0.9/0.35
    assert tractive_force(400, 13.0, 0.7) == pytest.approx(13_371.4, rel=1e-4)


@pytest.mark.parametrize("fn,args", [
    (overall_ratio, (0, 3.73)),
    (rpm_after_shift, (6000, 0, 2)),
    (tire_diameter_from_size, (265, 0, 17)),
    (tractive_force, (400, 13, 0.7, 1.5)),
])
def test_invalid(fn, args):
    with pytest.raises(ValueError):
        fn(*args)
