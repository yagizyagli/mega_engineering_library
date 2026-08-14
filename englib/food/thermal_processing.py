"""
Mega Engineering Library - Food Engineering: Thermal Processing Module
Handles microbial destruction kinetics, D-values, z-values, and thermal sterilization timing.
Validated against standard food engineering literature (e.g., Singh & Heldman's Introduction to Food Engineering).
"""

import math
from englib.common.exceptions import PhysicalBoundaryError, GeometricViolationError

class FoodThermalProcessing:

    @staticmethod
    def calculate_microbial_destruction_time(initial_population: float, final_population: float, d_value_minutes: float) -> float:
        """
        Calculates the total thermal processing time (t) required to reduce a microbial population to a target level.
        Based on first-order reaction kinetics: t = D * log10(N0 / N)
        Unit: Minutes (min)
        """
        if initial_population <= 0 or final_population <= 0:
            raise PhysicalBoundaryError("Microbial population counts (N0, N) must be positive non-zero values.")
        if initial_population < final_population:
            raise PhysicalBoundaryError("Physically impossible profile: Target population cannot exceed initial microbial load during sterilization.")
        if d_value_minutes <= 0:
            raise PhysicalBoundaryError("The decimal reduction time (D-value) must be a positive non-zero physical property.")

        return d_value_minutes * math.log10(initial_population / final_population)

    @staticmethod
    def calculate_temperature_dependent_d_value(reference_d_value: float, reference_temperature: float, target_temperature: float, z_value: float) -> float:
        """
        Calculates the new D-value at a target processing temperature based on the system's thermal resistance z-value.
        D = D_ref * 10^((T_ref - T) / z)
        """
        if reference_d_value <= 0 or z_value <= 0:
            raise PhysicalBoundaryError("Reference D-value and microbial thermal resistance (z-value) must be positive.")
            
        temperature_difference = reference_temperature - target_temperature
        return reference_d_value * (10.0 ** (temperature_difference / z_value))
