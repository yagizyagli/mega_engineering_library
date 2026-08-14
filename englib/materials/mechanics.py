"""
Mega Engineering Library - Materials Science & Engineering: Fracture Mechanics Module
Handles brittle fracture thresholds, critical stress propagation, and elastic strain energy.
Validated against standard materials fracture literature (e.g., Anderson's Fracture Mechanics).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class MaterialsMechanics:

    @staticmethod
    def calculate_griffith_critical_fracture_stress(elastic_modulus: float, specific_surface_energy: float, crack_length_meters: float) -> float:
        """
        Calculates the critical stress (sigma_c) required for unstable brittle crack propagation in a material.
        Based on Griffith's Fracture Criterion for a plane stress condition.
        sigma_c = sqrt( (2 * E * gamma) / (pi * a) )
        Unit: Pascals (Pa)
        """
        if crack_length_meters <= 0:
            raise GeometricViolationError("Internal crack length radius (a) must be a positive non-zero dimension.")
        if elastic_modulus <= 0 or specific_surface_energy <= 0:
            raise PhysicalBoundaryError("Material Young's modulus (E) and surface energy (gamma) must be positive values.")

        numerator = 2.0 * elastic_modulus * specific_surface_energy
        denominator = math.pi * crack_length_meters
        
        return math.sqrt(numerator / denominator)
