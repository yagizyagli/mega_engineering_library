"""
Mega Engineering Library - Aerospace Engineering: Propulsion Module
Handles jet engines, gas turbine cycles, nozzle fluid thermal dynamics, and rocket mechanics.
Validated against standard aerospace propulsion literature (e.g., Hill & Peterson, Mattingly).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class AerospacePropulsion:

    @staticmethod
    def calculate_rocket_delta_v(specific_impulse_seconds: float, initial_mass: float, final_mass: float) -> float:
        """
        Calculates the maximum change in velocity (Delta-V) using the Tsiolkovsky Rocket Equation.
        Delta-V = Isp * g0 * ln(m0 / mf)
        Unit: Meters per second (m/s)
        """
        if specific_impulse_seconds <= 0:
            raise PhysicalBoundaryError("Specific impulse (Isp) must be a positive non-zero parameter.")
        if final_mass <= 0:
            raise GeometricViolationError("Final dry mass (mf) of the spacecraft must be greater than zero.")
        if initial_mass < final_mass:
            raise PhysicalBoundaryError("Initial wet mass (m0) cannot be less than the dry structural mass.")

        g0 = 9.80665  # Standard Earth gravitational acceleration reference
        mass_ratio = initial_mass / final_mass
        return specific_impulse_seconds * g0 * math.log(mass_ratio)

    @staticmethod
    def calculate_thrust_jet_engine(air_mass_flow: float, exhaust_velocity: float, flight_velocity: float) -> float:
        """
        Calculates the net uninstalled thrust (F) of an ideal air-breathing jet engine.
        F = m_dot_air * (V_exhaust - V_flight)
        Unit: Newtons (N)
        """
        if air_mass_flow < 0:
            raise PhysicalBoundaryError("Air mass flow rate cannot be negative.")
        if exhaust_velocity < 0 or flight_velocity < 0:
            raise PhysicalBoundaryError("Velocities within the continuum must be non-negative values.")
        if exhaust_velocity < flight_velocity:
            # It produces drag, not thrust. Aviation limit warning.
            pass

        return air_mass_flow * (exhaust_velocity - flight_velocity)
