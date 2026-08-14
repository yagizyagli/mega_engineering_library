"""
Mega Engineering Library - Civil Engineering: Statics Module
Handles rigid-body equilibrium, force systems, moments, and internal beam forces.
Validated against standard structural mechanics literature (e.g., Hibbeler, Beer & Johnston).
"""

import math
from typing import Tuple, List, Dict
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class CivilStatics:

    @staticmethod
    def calculate_moment_2d(force: float, perpendicular_distance: float) -> float:
        """
        Calculates the magnitude of a 2D moment (torque) about a specific point.
        Moment = Force * Perpendicular Distance (M = F * d)
        Unit: Newton-meters (N·m)
        """
        if perpendicular_distance < 0:
            raise GeometricViolationError("Perpendicular distance for moment arm cannot be negative.")
        return force * perpendicular_distance

    @staticmethod
    def solve_simply_supported_beam_reactions(length: float, point_load: float, load_position: float) -> Tuple[float, float]:
        """
        Calculates the vertical reaction forces (Ry1, Ry2) for a simply supported 2D beam 
        with a single concentrated point load.
        
        Beam Layout:
        Pin Support (Ry1) at x = 0  ----------  Roller Support (Ry2) at x = Length
                                      |
                                  Point Load at x = load_position
                                  
        Returns:
            Tuple[float, float]: (Reaction force at Support 1, Reaction force at Support 2)
        """
        if length <= 0:
            raise GeometricViolationError("Beam length must be greater than zero.")
        if load_position < 0 or load_position > length:
            raise GeometricViolationError("Load position must lie within the physical boundaries of the beam length.")
        if point_load < 0:
            raise PhysicalBoundaryError("Force magnitude for structural calculation must be positive.")

        # Sum of moments around Support 1 (x = 0) = 0 => Ry2 * length - point_load * load_position = 0
        ry2 = (point_load * load_position) / length
        # Sum of vertical forces = 0 => Ry1 + Ry2 - point_load = 0
        ry1 = point_load - ry2

        return ry1, ry2

    @staticmethod
    def resolve_force_components_2d(magnitude: float, angle_degrees: float) -> Tuple[float, float]:
        """
        Resolves a 2D force vector into its orthogonal Cartesian components (Fx, Fy).
        Fx = Magnitude * cos(theta)
        Fy = Magnitude * sin(theta)
        """
        if magnitude < 0:
            raise PhysicalBoundaryError("Force magnitude cannot be negative.")
            
        angle_radians = math.radians(angle_degrees)
        fx = magnitude * math.cos(angle_radians)
        fy = magnitude * math.sin(angle_radians)
        
        return fx, fy
