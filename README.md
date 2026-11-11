# Drivetrain Gear Calculator

A tested Python library for drivetrain gearing: overall ratios, shift RPM drop, tire size from the sidewall code, road speed, cruise RPM, pulling force at the tire, and what bigger tires really do to a vehicle.

Built by an ASE-certified automotive technician to answer customer questions ("why is my truck slower and my speedometer wrong after bigger tires?") with numbers.

## The math

**Overall ratio:** $i = i_{gear} \cdot i_{final}$

**Tire diameter from size** (e.g. 265/70R17): $D = d_{rim} + 2 \cdot \frac{W \cdot AR}{100}$

**Road speed:** $v = \frac{RPM}{i} \cdot \frac{\pi D}{60}$

**RPM after a shift** (same road speed): $RPM_2 = RPM_1 \cdot \frac{i_2}{i_1}$

**Tractive force:** $F = \frac{T_{engine} \cdot i \cdot \eta}{r_{tire}}$

**Effective final drive after a tire change:** $i_{eff} = i_{final} \cdot \frac{D_{old}}{D_{new}}$

**Real speed with an uncorrected speedometer:** $v_{actual} = v_{indicated} \cdot \frac{D_{new}}{D_{old}}$

## Example

```bash
python examples/truck_tire_upgrade.py
```

```
Tire diameter:          31.6 in -> 33.8 in
Effective final drive:  3.55 -> 3.32
Speedo reads 70 mph:    actually 74.9 mph (+7.0%)
RPM at a true 70 mph:   1691 -> 1580 (10th gear)
1st gear pull:          24,317 N -> 22,718 N (-6.6%)
1-2 shift at 5500 rpm:  drops to 3499 rpm
Top of 1st at 5500 rpm: 33 mph
```

This is a pickup with a 10-speed automatic going from 265/70R17 to 285/75R17 tires. The truck loses about 7% of its pulling force in every gear and reads about 7% slow. That's why a re-gear (for example 3.55 to 3.73) or a speedometer recalibration is often recommended after a tire upgrade.

## Shop takeaways

- **Bigger tires act like a taller (lower number) axle ratio.** You get less pull, slower acceleration, and the transmission may hunt between gears.
- **The speedometer reads slow,** so the driver is going faster than shown. That's a ticket risk, and it also throws off odometer and service intervals.
- **RPM drop on an upshift** depends only on the ratio of the two gears, which is why close-ratio transmissions keep the engine in its power band.

## Install and test

```bash
pip install pytest
pytest -q
```

## How this was built

1. **Started from real customer questions** about tire upgrades, speedometer error, gearing, and "my truck feels slower."
2. **Split the problem** into ratios and tire geometry (`gearing.py`) and speed and force (`performance.py`). Everything uses SI units, and invalid inputs are rejected.
3. **Checked by hand.** For example, 265/70R17 works out to 31.6 in, 30.5 in to 33 in tires changes a 3.73 to an effective 3.45, and 60 mph indicated is really 64.9 mph. 10 pytest tests check these and a speed-to-RPM round trip.
4. **Ran a worked example.** The output above comes from actually running it.

**Limits:** no tire slip, aero drag, rolling resistance, or torque converter multiplication, and a fixed driveline efficiency of 90%.

## License

MIT
