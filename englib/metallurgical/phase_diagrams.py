"""
Mega Engineering Library - Metallurgical Engineering: Phase Transformations & Solidification Module
Handles alloy solidification cooling curves, nucleations, and phase transformation kinetics.
Validated against standard physical metallurgy literature (e.g., Porter & Easterling's Phase Transformations in Metals and Alloys).
"""

import math
from englib.common.exceptions import PhysicalBoundaryError

class MetallurgicalPhaseDiagrams:

    @staticmethod
    def calculate_avrami_phase_transformation_fraction(rate_constant_k: float, avrami_exponent_n: float, time_seconds: float) -> float:
        """
        Calculates the fraction of transformation (Y) during a solid-state phase change using the Avrami Equation.
        Y = 1 - exp(-k * t^n)
        Returns a fraction value strictly bounded between 0.0 and 1.0.
        """
        if rate_constant_k <= 0 or avrami_exponent_n <= 0:
            raise PhysicalBoundaryError("Avrami kinetic rate constants (k) and structural exponents (n) must be positive.")
        if time_seconds < 0:
            raise PhysicalBoundaryError("Time context duration cannot be negative.")

        transformed_fraction = 1.0 - math.exp(-rate_constant_k * (time_seconds ** avrami_exponent_n))
        
        # Truncation boundary safety check
        return max(0.0, min(1.0, transformed_fraction))
