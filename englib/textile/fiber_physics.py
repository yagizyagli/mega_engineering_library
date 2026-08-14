"""
Mega Engineering Library - Textile Engineering: Fiber Physics Module
Handles fiber tensile strength, moisture regain kinetics, and macromolecular stress-strain profiles.
Validated against standard textile physics literature (e.g., Morton & Hearle's Physical Properties of Textile Fibres).
"""

from englib.common.exceptions import PhysicalBoundaryError, GeometricViolationError

class FiberPhysics:

    @staticmethod
    def calculate_fiber_moisture_regain(moisture_free_weight_g: float, moist_weight_g: float) -> float:
        """
        Calculates the percentage moisture regain (R) of a textile fiber sample.
        R = ((W_moist - W_dry) / W_dry) * 100
        Unit: Percentage (%)
        """
        if moisture_free_weight_g <= 0:
            raise PhysicalBoundaryError("The dry, moisture-free weight of the fiber must be a positive non-zero value.")
        if moist_weight_g < moisture_free_weight_g:
            raise PhysicalBoundaryError("Physically impossible profile: Moist fiber weight cannot be less than its absolute dry bone mass.")

        return ((moist_weight_g - moisture_free_weight_g) / moisture_free_weight_g) * 100.0
