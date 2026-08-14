"""
Mega Engineering Library - Aerospace Engineering: Orbital Mechanics Module
Handles Keplerian orbits, spacecraft velocity vectors, and planetary escape trajectories.
Validated against standard astrodynamics literature (e.g., Curtis's Orbital Mechanics for Engineering Students).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class OrbitalMechanics:

    @staticmethod
    def calculate_orbital_velocity_vis_viva(gravitational_parameter_mu: float, radial_distance: float, semi_major_axis: float) -> float:
        """
        Calculates the velocity (v) of a spacecraft in a Keplerian orbit using the Vis-Viva Equation.
        v = sqrt( mu * (2/r - 1/a) )
        Where:
        mu = Standard gravitational parameter of the central body (e.g., Earth's mu = 3.986004418e14 m³/s²)
        r = Radial distance from the central body center
        a = Semi-major axis of the orbit (positive for ellipses, negative for hyperbolas, infinite for parabolas)
        Unit: Meters per second (m/s)
        """
        if radial_distance <= 0:
            raise GeometricViolationError("Radial distance from the planetary core center must be greater than zero.")
        if gravitational_parameter_mu <= 0:
            raise PhysicalBoundaryError("Standard gravitational parameter (mu) must be positive.")
        if semi_major_axis <= 0:
            raise GeometricViolationError("This elliptical routine requires a positive non-zero semi-major axis.")

        energy_term = (2.0 / radial_distance) - (1.0 / semi_major_axis)
        if energy_term < 0:
            raise PhysicalBoundaryError("Physically impossible orbital configuration: Energy terms result in negative kinetic profiles.")

        return math.sqrt(gravitational_parameter_mu * energy_term)

    @staticmethod
    def calculate_escape_velocity(gravitational_parameter_mu: float, radial_distance: float) -> float:
        """
        Calculates the escape velocity (v_esc) required to break free from a planet's gravitational field.
        v_esc = sqrt( (2 * mu) / r )
        Unit: Meters per second (m/s)
        """
        if radial_distance <= 0:
            raise GeometricViolationError("Radial distance from the planetary center must be greater than zero.")
        if gravitational_parameter_mu <= 0:
            raise PhysicalBoundaryError("Planetary gravitational parameter must be greater than zero.")

        return math.sqrt((2.0 * gravitational_parameter_mu) / radial_distance)
