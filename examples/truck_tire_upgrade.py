"""Worked example: pickup going from 265/70R17 to 285/75R17 tires.

Run from the repo root:  python examples/truck_tire_upgrade.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from drivetrain import (effective_final_drive, overall_ratio, road_speed,  # noqa: E402
                        rpm_after_shift, rpm_at_speed, speedometer_error,
                        tire_diameter_from_size, tractive_force)

MPH = 0.44704
first, second, top = 4.70, 2.99, 0.64   # 10-speed automatic, selected gears
final = 3.55
torque = 650                             # N*m peak engine torque

old_d = tire_diameter_from_size(265, 70, 17)
new_d = tire_diameter_from_size(285, 75, 17)
e = speedometer_error(70, old_d, new_d)

cruise_old = rpm_at_speed(70 * MPH, overall_ratio(top, final), old_d)
cruise_new = rpm_at_speed(70 * MPH, overall_ratio(top, final), new_d)
pull_old = tractive_force(torque, overall_ratio(first, final), old_d)
pull_new = tractive_force(torque, overall_ratio(first, final), new_d)

print(f"Tire diameter:          {old_d / 0.0254:.1f} in -> {new_d / 0.0254:.1f} in")
print(f"Effective final drive:  {final} -> {effective_final_drive(final, old_d, new_d):.2f}")
print(f"Speedo reads 70 mph:    actually {e['actual']:.1f} mph ({e['error_pct']:+.1f}%)")
print(f"RPM at a true 70 mph:   {cruise_old:.0f} -> {cruise_new:.0f} (10th gear)")
print(f"1st gear pull:          {pull_old:,.0f} N -> {pull_new:,.0f} N "
      f"({(pull_new / pull_old - 1) * 100:+.1f}%)")
print(f"1-2 shift at 5500 rpm:  drops to {rpm_after_shift(5500, first, second):.0f} rpm")
print(f"Top of 1st at 5500 rpm: {road_speed(5500, overall_ratio(first, final), new_d) / MPH:.0f} mph")
