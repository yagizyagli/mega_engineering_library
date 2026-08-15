"""
Mega Engineering Library - Mechanical Engineering: Solid Mechanics Module
Handles normal stress, strain, axial deformation, and material failure indices.
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class SolidMechanics:

    @staticmethod
    def calculate_axial_stress(force: float, area: float) -> float:
        """Calculates normal axial stress (sigma = F/A)."""
        if area <= 0:
            raise GeometricViolationError("Cross-sectional area must be positive.")
        return force / area

    @staticmethod
    def calculate_axial_deformation(force: float, length: float, area: float, elastic_modulus: float) -> float:
        """Calculates total linear elongation under axial loads."""
        if length <= 0 or area <= 0 or elastic_modulus <= 0:
            raise GeometricViolationError("Physical and material limits must be positive non-zero parameters.")
        return (force * length) / (area * elastic_modulus)
