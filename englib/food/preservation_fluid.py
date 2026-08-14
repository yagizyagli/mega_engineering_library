"""
Mega Engineering Library - Food Engineering: Rheology & Preservation Fluid Module
Handles non-Newtonian food fluid viscosity modeling, shear stresses, and flow behaviors.
Validated against standard food process rheology metrics.
"""

from englib.common.exceptions import PhysicalBoundaryError, GeometricViolationError

class FoodRheology:

    @staticmethod
    def calculate_power_law_shear_stress(flow_behavior_index_n: float, consistency_coefficient_k: float, shear_rate_per_sec: float) -> float:
        """
        Calculates the shear stress (tau) of a non-Newtonian food fluid using the Power Law model.
        tau = K * (gamma_dot ^ n)
         fluid classifications based on index 'n':
        - n < 1.0: Pseudoplastic / Shear-thinning (e.g., applesauce, ketchup)
        - n == 1.0: Newtonian (e.g., water, sugar solutions)
        - n > 1.0: Dilatant / Shear-thickening (e.g., cornstarch suspensions)
        Unit: Pascals (Pa)
        """
        if consistency_coefficient_k <= 0:
            raise PhysicalBoundaryError("Fluid consistency coefficient (K) must be a positive non-zero physical parameter.")
        if shear_rate_per_sec < 0:
            raise PhysicalBoundaryError("Fluid shear rate cannot be negative.")
        if flow_behavior_index_n <= 0:
            raise PhysicalBoundaryError("Flow behavior index (n) must be a positive non-zero ratio.")

        return consistency_coefficient_k * (shear_rate_per_sec ** flow_behavior_index_n)
