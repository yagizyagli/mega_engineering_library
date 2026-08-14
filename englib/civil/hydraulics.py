"""
Mega Engineering Library - Civil Engineering: Hydraulics & Water Resources Module
Handles open channel flow, fluid transport infrastructure, and pipe network hydraulics.
Validated against standard hydraulic engineering literature (e.g., Chaudhry, Chow).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class CivilHydraulics:

    @staticmethod
    def calculate_manning_open_channel_velocity(manning_n: float, hydraulic_radius: float, channel_slope: float) -> float:
        """
        Calculates the uniform steady-state flow velocity (V) in an open channel using Manning's Equation.
        V = (1 / n) * (R_h ^ (2/3)) * (S ^ (1/2))
        Unit: Meters per second (m/s)
        """
        if manning_n <= 0:
            raise PhysicalBoundaryError("Manning's roughness coefficient (n) must be a positive non-zero value.")
        if hydraulic_radius <= 0:
            raise GeometricViolationError("Hydraulic radius (Rh) must be greater than zero.")
        if channel_slope <= 0:
            raise GeometricViolationError("Channel longitudinal slope (S) must be positive and non-zero for gravity flow.")

        velocity = (1.0 / manning_n) * (hydraulic_radius ** (2.0 / 3.0)) * (channel_slope ** 0.5)
        return velocity

    @staticmethod
    def calculate_circular_pipe_hydraulic_radius(diameter: float) -> float:
        """
        Calculates the hydraulic radius (Rh) of a circular pipe running completely full.
        Rh = Area / Wetted Perimeter = (pi * D^2 / 4) / (pi * D) = D / 4
        Unit: Meters (m)
        """
        if diameter <= 0:
            raise GeometricViolationError("Pipe diameter must be a positive non-zero dimension.")
            
        return diameter / 4.0
