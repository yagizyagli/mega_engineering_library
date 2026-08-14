"""
Mega Engineering Library - Mechatronics & Robotics Engineering: Dynamics Module
Handles rigid body acceleration, multi-link inertia matrices, and torque/force requirements.
Validated against standard robotics dynamics literature (e.g., Spong, Hutchinson, Vidyasagar).
"""

import math
from typing import Tuple
from englib.common.constants import GRAVITY
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class RoboticDynamics:

    @staticmethod
    def calculate_link_inertia_cylinder(mass: float, radius: float, length: float) -> Tuple[float, float, float]:
        """
        Calculates the principal moments of inertia (Ix, Iy, Iz) for a solid uniform cylindrical robot link.
        Assumes the Z-axis aligns with the length of the cylinder.
        Iz = 0.5 * m * r^2
        Ix = Iy = (1/12) * m * L^2 + (1/4) * m * r^2
        Unit: kg·m²
        """
        if mass <= 0:
            raise PhysicalBoundaryError("Link mass must be a positive non-zero value.")
        if radius <= 0 or length <= 0:
            raise GeometricViolationError("Link geometric dimensions (radius and length) must be positive.")

        iz = 0.5 * mass * (radius ** 2)
        ix_y = (1.0 / 12.0) * mass * (length ** 2) + (0.25 * mass * (radius ** 2))
        
        return ix_y, ix_y, iz

    @staticmethod
    def calculate_gravity_torque_1r(mass: float, length_to_center_of_mass: float, theta_degrees: float) -> float:
        """
        Calculates the holding torque required at a single rotary joint (1-R) to counteract gravity.
        Torque = m * g * r * cos(theta)
        Where theta is measured from the horizontal plane.
        Unit: Newton-meters (N·m)
        """
        if mass <= 0:
            raise PhysicalBoundaryError("Link mass cannot be zero or negative.")
        if length_to_center_of_mass <= 0:
            raise GeometricViolationError("Distance to link center of mass must be positive.")

        theta_rad = math.radians(theta_degrees)
        torque = mass * GRAVITY * length_to_center_of_mass * math.cos(theta_rad)
        return torque
