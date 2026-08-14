"""
Mega Engineering Library - Civil Engineering: Structural Dynamics & Earthquake Engineering Module
Handles structural responses to dynamic loadings, seismic base shear, and modal periods.
Validated against standard structural dynamics literature (e.g., Chopra, Clough & Penzien).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class StructuralDynamics:

    @staticmethod
    def calculate_structural_period(mass: float, stiffness: float) -> float:
        """
        Calculates the fundamental natural period (T) of a single-degree-of-freedom (SDOF) structure.
        T = 2 * pi * sqrt(m / k)
        Unit: Seconds (s)
        """
        if mass <= 0:
            raise PhysicalBoundaryError("Structural mass must be a positive non-zero value.")
        if stiffness <= 0:
            raise PhysicalBoundaryError("Structural lateral stiffness (k) must be greater than zero.")

        return 2.0 * math.pi * math.sqrt(mass / stiffness)

    @staticmethod
    def calculate_seismic_base_shear_equivalent_lateral(seismic_response_coefficient: float, total_dead_weight: float) -> float:
        """
        Calculates the total design lateral seismic force at the base of a structure (Base Shear, V).
        Based on the Equivalent Lateral Force Procedure (ASCE 7 / Eurocode 8 principles).
        V = Cs * W
        Unit: Kilonewtons (kN) or Newtons (N)
        """
        if seismic_response_coefficient < 0 or seismic_response_coefficient > 2.0:
            raise PhysicalBoundaryError("Seismic response coefficient (Cs) must be within realistic physical boundaries (0 to 2.0).")
        if total_dead_weight <= 0:
            raise PhysicalBoundaryError("Total effective seismic weight (W) of the structure must be positive.")

        return seismic_response_coefficient * total_dead_weight

    @staticmethod
    def calculate_damped_natural_frequency(undamped_frequency: float, damping_ratio: float) -> float:
        """
        Calculates the damped natural frequency (omega_d) of a building structure under dynamic wind/seismic excitation.
        omega_d = omega_n * sqrt(1 - zeta^2)
        Valid only for underdamped structures (zeta < 1.0), which represents almost all civil engineering structures.
        """
        if undamped_frequency <= 0:
            raise PhysicalBoundaryError("Undamped natural frequency must be positive.")
        if damping_ratio < 0 or damping_ratio >= 1.0:
            raise PhysicalBoundaryError("Civil structures must be underdamped (0 <= damping_ratio < 1.0).")

        return undamped_frequency * math.sqrt(1.0 - (damping_ratio ** 2))
