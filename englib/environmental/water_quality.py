"""
Mega Engineering Library - Environmental Engineering: Water Quality Modeling Module
Handles aquatic oxygen depletion profiles and river self-purification kinetics.
Validated against standard environmental engineering literature (e.g., Chapra's Surface Water Quality Modeling).
"""

import math
from englib.common.exceptions import PhysicalBoundaryError

class WaterQuality:

    @staticmethod
    def calculate_streeter_phelps_oxygen_deficit(initial_deficit_mg_l: float, initial_bod_mg_l: float, deoxygenation_rate_per_day: float, reaeration_rate_per_day: float, time_days: float) -> float:
        """
        Calculates the dissolved oxygen (DO) deficit (D) in a river downstream from a waste discharge point.
        Based on the classical Streeter-Phelps stream purification model.
        D = (kd * L0 / (kr - kd)) * (exp(-kd * t) - exp(-kr * t)) + D0 * exp(-kr * t)
        Unit: Milligrams per liter (mg/L)
        """
        if deoxygenation_rate_per_day <= 0 or reaeration_rate_per_day <= 0:
            raise PhysicalBoundaryError("Deoxygenation (kd) and reaeration (kr) kinetic constants must be positive values.")
        if time_days < 0 or initial_bod_mg_l < 0 or initial_deficit_mg_l < 0:
            raise PhysicalBoundaryError("Time coordinates and initial biochemical oxygen profiles cannot be negative.")

        if deoxygenation_rate_per_day == reaeration_rate_per_day:
            # Mathematical guard for identical rates to avoid division by zero
            reaeration_rate_per_day += 1e-6

        coefficient = (deoxygenation_rate_per_day * initial_bod_mg_l) / (reaeration_rate_per_day - deoxygenation_rate_per_day)
        kinetic_term = math.exp(-deoxygenation_rate_per_day * time_days) - math.exp(-reaeration_rate_per_day * time_days)
        initial_term = initial_deficit_mg_l * math.exp(-reaeration_rate_per_day * time_days)

        return (coefficient * kinetic_term) + initial_term
