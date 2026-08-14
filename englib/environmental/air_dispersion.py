"""
Mega Engineering Library - Environmental Engineering: Air Dispersion Modeling Module
Handles atmospheric pollutant plume tracking, industrial emissions, and gas concentrations.
Validated against standard environmental science literature (e.g., Turner's Atmospheric Dispersion Estimates).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class AirDispersion:

    @staticmethod
    def calculate_gaussian_plume_centerline_concentration(emission_rate_g_s: float, wind_speed_m_s: float, sigma_y_meters: float, sigma_z_meters: float, effective_stack_height_meters: float) -> float:
        """
        Calculates the steady-state pollutant concentration (C) directly downwind along the plume centerline (y=0, z=0).
        Based on the classical Gaussian Plume Dispersion Equation.
        C = (Q / (2 * pi * u * sigma_y * sigma_z)) * exp(-0.5 * (H / sigma_z)^2)
        Unit: Grams per cubic meter (g/m³)
        """
        if wind_speed_m_s <= 0:
            raise PhysicalBoundaryError("Wind speed (u) at stack height must be a positive non-zero velocity.")
        if sigma_y_meters <= 0 or sigma_z_meters <= 0:
            raise GeometricViolationError("Atmospheric dispersion coefficients (sigma) must be positive values to avoid division by zero.")
        if emission_rate_g_s < 0:
            raise PhysicalBoundaryError("Source pollutant emission rate (Q) cannot be negative.")
        if effective_stack_height_meters < 0:
            raise GeometricViolationError("Effective chimney/stack height (H) cannot be negative.")

        denominator = 2.0 * math.pi * wind_speed_m_s * sigma_y_meters * sigma_z_meters
        mass_term = emission_rate_g_s / denominator
        
        exponential_term = math.exp(-0.5 * ((effective_stack_height_meters / sigma_z_meters) ** 2))
        return mass_term * exponential_term
