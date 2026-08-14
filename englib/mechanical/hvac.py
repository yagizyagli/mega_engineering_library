"""
Mega Engineering Library - Mechanical Engineering: HVAC Systems Module
Handles building thermal envelope loads, heat gain, ventilation math, and psychrometric properties.
Validated against standard ASHRAE guidelines and thermal environmental engineering manuals.
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class HVACSystems:

    @staticmethod
    def calculate_overall_heat_transfer_coefficient(r_values: list[float]) -> float:
        """
        Calculates the overall heat transfer coefficient (U-value) for a multi-layered building wall.
        Total R_thermal = R1 + R2 + ... + Rn
        U = 1 / Total R_thermal
        Unit: W/(m²·K)
        """
        if not r_values:
            raise ValueError("Thermal resistance (R-value) layer list cannot be empty.")
            
        total_r = 0.0
        for r in r_values:
            if r <= 0:
                raise PhysicalBoundaryError("Thermal resistance layers must possess positive non-zero values.")
            total_r += r
            
        return 1.0 / total_r

    @staticmethod
    def calculate_sensible_heat_load_air(volume_flow_rate_m3_s: float, temperature_diff_celsius: float, air_density: float = 1.2, specific_heat_air: float = 1005.0) -> float:
        """
        Calculates the sensible heat load (Q_sensible) required to heat or cool an air stream.
        Q = m_dot * Cp * delta_T = (rho * V_dot) * Cp * delta_T
        Unit: Watts (W)
        """
        if volume_flow_rate_m3_s < 0:
            raise GeometricViolationError("Volumetric air flow rate cannot be negative.")
        if air_density <= 0 or specific_heat_air <= 0:
            raise PhysicalBoundaryError("Air density and specific heat parameters must be positive physical constants.")

        mass_flow_rate = air_density * volume_flow_rate_m3_s
        return mass_flow_rate * specific_heat_air * temperature_diff_celsius
