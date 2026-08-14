"""
Mega Engineering Library - Aerospace Engineering: Flight Dynamics & Control Module
Handles rigid aircraft stability derivatives, static margins, and trim state evaluations.
Validated against standard flight mechanics literature (e.g., Nelson's Flight Stability and Automatic Control).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class FlightDynamics:

    @staticmethod
    def calculate_aircraft_static_margin(center_of_gravity: float, aerodynamic_center: float, mean_aerodynamic_chord: float) -> float:
        """
        Calculates the static margin (SM) of an fixed-wing aircraft configuration.
        A positive static margin implies longitudinal static stability.
        SM = (X_ac - X_cg) / c
        Returns a dimensionless ratio (e.g., 0.10 means a 10% static margin).
        """
        if mean_aerodynamic_chord <= 0:
            raise GeometricViolationError("Mean Aerodynamic Chord (c) must be a positive non-zero length metric.")
        if center_of_gravity < 0 or aerodynamic_center < 0:
            raise GeometricViolationError("Reference frame positions from the nose datum must be positive.")

        static_margin = (aerodynamic_center - center_of_gravity) / mean_aerodynamic_chord
        return static_margin
