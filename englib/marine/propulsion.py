"""
Mega Engineering Library - Marine Engineering & Naval Architecture: Propulsion Module
Handles propeller open-water performance parameters, thrust forces, and cavitation safety margins.
Validated against standard marine propulsion principles.
"""

from englib.common.exceptions import PhysicalBoundaryError

class MarinePropulsion:

    @staticmethod
    def calculate_propeller_advance_coefficient(forward_velocity_m_s: float, rotational_speed_rps: float, propeller_diameter_meters: float) -> float:
        """
        Calculates the dimensionless Propeller Advance Coefficient (J).
        J = V_advance / (n * D)
        """
        if rotational_speed_rps <= 0:
            raise PhysicalBoundaryError("Propeller rotational shaft speed (n) must be a positive non-zero RPS profile.")
        if propeller_diameter_meters <= 0:
            raise PhysicalBoundaryError("Propeller blade diameter (D) must be greater than zero.")
        if forward_velocity_m_s < 0:
            raise PhysicalBoundaryError("Advance speed through the wake cannot be negative.")

        return forward_velocity_m_s / (rotational_speed_rps * propeller_diameter_meters)
