"""
Mega Engineering Library - Transportation Engineering: Pavement Design Module
Handles flexible/rigid pavement layers, structural numbers, and load design indices.
Validated against standard pavement design guidelines (e.g., AASHTO Pavement Design Guide, Huang).
"""

from typing import List
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class PavementDesign:

    @staticmethod
    def calculate_aashto_flexible_structural_number(layer_coefficients: List[float], layer_thicknesses_inches: List[float]) -> float:
        """
        Calculates the overall Structural Number (SN) for a multi-layered flexible asphalt pavement layout.
        SN = a1*D1 + a2*D2 + a3*D3 + ...
        Where:
        a_i = Layer empirical material drainage coefficients
        D_i = Layer actual structural thicknesses in inches
        """
        if not layer_coefficients or not layer_thicknesses_inches:
            raise ValueError("Pavement layer structural coefficients and thicknesses arrays cannot be empty.")
        if len(layer_coefficients) != len(layer_thicknesses_inches):
            raise GeometricViolationError("Mismatched infrastructure arrays: The number of coefficients must match thickness profiles.")

        for a, d in zip(layer_coefficients, layer_thicknesses_inches):
            if a < 0 or d < 0:
                raise PhysicalBoundaryError("Pavement material layer drainage metrics and physical dimensions cannot be negative.")

        return sum(a * d for a, d in zip(layer_coefficients, layer_thicknesses_inches))
