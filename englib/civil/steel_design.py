"""
Mega Engineering Library - Civil Engineering: Steel Design Module
Handles structural steel design formulas, column buckling limits, and tensile capacities.
Validated against standard structural steel literature (e.g., AISC 360, Eurocode 3).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class SteelDesign:

    @staticmethod
    def calculate_euler_buckling_load(elastic_modulus: float, moment_of_inertia: float, effective_length: float) -> float:
        """
        Calculates the critical Euler buckling load (Pcr) for an ideal pin-ended structural steel column.
        Pcr = (pi^2 * E * I) / (Le^2)
        Unit: Newtons (N)
        """
        if effective_length <= 0:
            raise GeometricViolationError("Effective column length (Le) must be a positive non-zero value.")
        if moment_of_inertia <= 0:
            raise GeometricViolationError("Area moment of inertia (I) must be greater than zero.")
        if elastic_modulus <= 0:
            raise PhysicalBoundaryError("Modulus of Elasticity (E) for steel must be a positive physical property.")

        critical_load = (math.pi ** 2 * elastic_modulus * moment_of_inertia) / (effective_length ** 2)
        return critical_load

    @staticmethod
    def calculate_slenderness_ratio(effective_length: float, radius_of_gyration: float) -> float:
        """
        Calculates the dimensionless slenderness ratio (lambda) of a compression member.
        lambda = Le / r
        Generally, AISC specifies lambda <= 200 for compression members.
        """
        if effective_length <= 0:
            raise GeometricViolationError("Effective length must be positive.")
        if radius_of_gyration <= 0:
            raise GeometricViolationError("Radius of gyration (r) must be a positive non-zero cross-sectional property.")

        return effective_length / radius_of_gyration

    @staticmethod
    def calculate_nominal_tensile_yield_capacity(gross_area: float, yield_strength: float) -> float:
        """
        Calculates the nominal tensile yield strength (Pn) of a steel member on the gross cross-section area.
        Pn = Ag * fy
        Unit: Newtons (N)
        """
        if gross_area <= 0:
            raise GeometricViolationError("Gross cross-sectional area (Ag) must be greater than zero.")
        if yield_strength <= 0:
            raise PhysicalBoundaryError("Steel yield strength (fy) must be a positive property.")

        return gross_area * yield_strength
