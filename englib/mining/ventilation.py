"""
Mega Engineering Library - Mining & Geological Engineering: Mine Ventilation Module
Handles airway friction losses, mine fan ventilation dynamics, and fluid resistance layouts underground.
Validated against standard subsurface ventilation manuals (e.g., Hartman's Mine Ventilation and Air Conditioning).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class MineVentilation:

    @staticmethod
    def calculate_atkinson_friction_loss(atkinson_k_factor: float, perimeter: float, length: float, velocity: float, cross_sectional_area: float) -> float:
        """
        Calculates the total ventilation pressure drop (p) in a mine airway tunnel using the Atkinson Equation.
        p = (K * O * L * V^2) / A
        Where:
        K = Atkinson friction factor
        O = Airway wetted perimeter
        L = Airway tunnel length
        V = Air velocity
        A = Cross-sectional area of the airway
        Unit: Pascals (Pa)
        """
        if cross_sectional_area <= 0:
            raise GeometricViolationError("Mine airway cross-sectional area (A) must be a positive non-zero metric.")
        if length <= 0 or perimeter <= 0:
            raise GeometricViolationError("Airway geometric profiles (length and perimeter) must be positive.")
        if atkinson_k_factor <= 0:
            raise PhysicalBoundaryError("Atkinson friction factor (K) must be positive based on airway wall roughness.")
        if velocity < 0:
            raise PhysicalBoundaryError("Air flow velocity inside the tunnel cannot be negative.")

        numerator = atkinson_k_factor * perimeter * length * (velocity ** 2)
        return numerator / cross_sectional_area
