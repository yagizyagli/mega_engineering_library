"""
Mega Engineering Library - Civil Engineering: Geotechnical Engineering Module
Provides analytical solutions for soil mechanics, bearing capacity of foundations, and soil properties.
Validated against standard geotechnical literature (e.g., Das, Terzaghi).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class GeotechnicalEngineering:

    @staticmethod
    def calculate_soil_void_ratio(volume_of_voids: float, volume_of_solids: float) -> float:
        """
        Calculates the dimensionless void ratio (e) of a soil sample.
        e = Vv / Vs
        """
        if volume_of_solids <= 0:
            raise GeometricViolationError("Volume of solid soil particles (Vs) must be greater than zero.")
        if volume_of_voids < 0:
            raise GeometricViolationError("Volume of voids (Vv) cannot be negative.")

        return volume_of_voids / volume_of_solids

    @staticmethod
    def calculate_terzaghi_bearing_capacity_strip_footing(cohesion: float, effective_stress: float, unit_weight: float, footing_width: float, nc: float, nq: float, ngamma: float) -> float:
        """
        Calculates the ultimate bearing capacity (qu) for a continuous (strip) shallow footing using Terzaghi's equation.
        qu = c*Nc + q*Nq + 0.5*gamma*B*Ngamma
        Unit: Pascals (Pa) or N/m²
        """
        if footing_width <= 0:
            raise GeometricViolationError("Footing width (B) must be a positive non-zero value.")
        if cohesion < 0 or effective_stress < 0 or unit_weight < 0:
            raise PhysicalBoundaryError("Soil physical properties (cohesion, stress, unit weight) cannot be negative.")
        if nc < 0 or nq < 0 or ngamma < 0:
            raise PhysicalBoundaryError("Terzaghi bearing capacity factors (Nc, Nq, Ngamma) must be non-negative.")

        term1 = cohesion * nc
        term2 = effective_stress * nq
        term3 = 0.5 * unit_weight * footing_width * ngamma

        return term1 + term2 + term3
