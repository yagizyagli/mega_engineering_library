"""
Mega Engineering Library - Mechanical Engineering: Heat Transfer Module
Provides analytical formulations for Conduction, Convection, Radiation, and Heat Exchangers.
Validated against standard thermal sciences literature (e.g., Incropera, Dewitt).
"""

import math
from englib.common.constants import PI
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class HeatTransfer:

    @staticmethod
    def calculate_conduction_plane_wall(thermal_conductivity: float, area: float, thickness: float, t_inside: float, t_outside: float) -> float:
        """
        Calculates steady-state 1D heat conduction rate (Q) through a plane wall.
        Fourier's Law: Q = (k * A * (T_in - T_out)) / L
        Unit: Watts (W)
        """
        if thickness <= 0 or area <= 0:
            raise GeometricViolationError("Wall dimensions (thickness and area) must be positive non-zero values.")
        if thermal_conductivity <= 0:
            raise PhysicalBoundaryError("Thermal conductivity (k) must be a positive physical property.")
            
        temperature_difference = t_inside - t_outside
        return (thermal_conductivity * area * temperature_difference) / thickness

    @staticmethod
    def calculate_convection_cooling(convection_coefficient: float, area: float, t_surface: float, t_fluid: float) -> float:
        """
        Calculates convective heat transfer rate (Q) between a solid surface and a moving fluid.
        Newton's Law of Cooling: Q = h * A * (T_surface - T_fluid)
        Unit: Watts (W)
        """
        if area <= 0:
            raise GeometricViolationError("Surface area must be greater than zero.")
        if convection_coefficient <= 0:
            raise PhysicalBoundaryError("Convective heat transfer coefficient (h) must be positive.")
            
        return convection_coefficient * area * (t_surface - t_fluid)

    @staticmethod
    def calculate_radiation_blackbody(area: float, temperature_kelvin: float) -> float:
        """
        Calculates the total emissive power (Q) from a perfect blackbody surface into space.
        Stefan-Boltzmann Law: Q = sigma * A * T^4
        Where sigma = 5.670374419e-8 W/(m²·K⁴)
        Unit: Watts (W)
        """
        if area <= 0:
            raise GeometricViolationError("Surface area must be positive.")
        if temperature_kelvin < 0:
            raise PhysicalBoundaryError("Absolute temperature for radiation calculation cannot be below zero Kelvin.")
            
        stefan_boltzmann_constant = 5.670374419e-8
        return stefan_boltzmann_constant * area * (temperature_kelvin ** 4)
