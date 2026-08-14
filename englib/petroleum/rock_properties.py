"""
Mega Engineering Library - Petroleum Engineering: Reservoir Rock Properties Module
Handles rock porosity, absolute/relative permeability, and formation electrical logs.
Validated against standard petrophysics literature (e.g., Tiab & Donaldson).
"""

import math
from englib.common.exceptions import PhysicalBoundaryError, GeometricViolationError

class ReservoirRockProperties:

    @staticmethod
    def calculate_water_saturation_archie(rock_tortuosity_a: float, water_resistivity: float, formation_resistivity: float, porosity: float, cementation_exponent_m: float, saturation_exponent_n: float) -> float:
        """
        Calculates the fractional water saturation (Sw) of a reservoir rock layer using Archie's Law.
        Sw = ( (a * Rw) / (Rt * (phi ^ m)) ) ^ (1 / n)
        Returns water saturation as a decimal fraction between 0.0 and 1.0.
        """
        if porosity <= 0.0 or porosity > 1.0:
            raise PhysicalBoundaryError("Rock matrix porosity (phi) must be a bounded ratio strictly between 0.0 and 1.0.")
        if water_resistivity <= 0 or formation_resistivity <= 0:
            raise PhysicalBoundaryError("Electrical resistivity parameters must be positive non-zero measurements.")
        if rock_tortuosity_a <= 0 or cementation_exponent_m <= 0 or saturation_exponent_n <= 0:
            raise GeometricViolationError("Empirical Archie matrix structural coefficients must be greater than zero.")

        denominator = formation_resistivity * (porosity ** cementation_exponent_m)
        if denominator == 0:
            raise ZeroDivisionError("Archie evaluation yielded a division by zero matrix error.")

        inner_term = (rock_tortuosity_a * water_resistivity) / denominator
        water_saturation = inner_term ** (1.0 / saturation_exponent_n)

        if water_saturation < 0.0 or water_saturation > 1.0:
            # Numerical truncation guard for edge case logging interpretations
            return max(0.0, min(1.0, water_saturation))

        return water_saturation
