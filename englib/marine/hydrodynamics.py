"""
Mega Engineering Library - Marine Engineering & Naval Architecture: Hydrodynamics Module
Handles ship hull fluid interactions, wave-making resistances, and Froude scaling ratios.
Validated against standard marine fluid mechanics manuals.
"""

import math
from englib.common.constants import GRAVITY
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class MarineHydrodynamics:

    @staticmethod
    def calculate_froude_number(ship_velocity_m_s: float, waterline_length_meters: float) -> float:
        """
        Calculates the dimensionless Froude Number (Fn) used to quantify ship hull wave-making resistance.
        Fn = V / sqrt(g * L)
        """
        if waterline_length_meters <= 0:
            raise GeometricViolationError("Ship waterline length (L) must be a positive non-zero metric.")
        if ship_velocity_m_s < 0:
            raise PhysicalBoundaryError("Ship true forward velocity cannot be negative.")

        denominator = math.sqrt(GRAVITY * waterline_length_meters)
        return ship_velocity_m_s / denominator
