"""
Mega Engineering Library - Nuclear Engineering: Thermal Hydraulics Module
Handles fuel element heat removal, heat fluxes, and core thermal safety limits.
Validated against standard nuclear thermal hydraulics literature (e.g., Todreas & Kazimi).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class NuclearThermalHydraulics:

    @staticmethod
    def calculate_fuel_element_heat_flux(linear_heat_generation_rate_w_m: float, fuel_rod_diameter_meters: float) -> float:
        """
        Calculates the surface heat flux (q") of a cylindrical nuclear fuel rod profile.
        q" = q_linear / (pi * D)
        Unit: Watts per square meter (W/m²)
        """
        if fuel_rod_diameter_meters <= 0:
            raise GeometricViolationError("Nuclear fuel rod cladding diameter must be a positive non-zero dimension.")
        if linear_heat_generation_rate_w_m < 0:
            raise PhysicalBoundaryError("Linear heat generation rate (q_linear) cannot be negative.")

        import math
        return linear_heat_generation_rate_w_m / (math.pi * fuel_rod_diameter_meters)
