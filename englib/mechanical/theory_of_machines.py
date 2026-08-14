"""
Mega Engineering Library - Mechanical Engineering: Theory of Machines & Vibrations Module
Handles kinematic linkages, degrees of freedom, and mechanical vibration analysis.
Validated against standard mechanical vibration literature (e.g., Rao, Thomson).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class TheoryOfMachines:

    @staticmethod
    def calculate_kutzbach_criterion_2d(links: int, joints_1_dof: int, joints_2_dof: int) -> int:
        """
        Calculates the Degrees of Freedom (Mobility, M) of a 2D planar mechanism using Kutzbach's Criterion.
        M = 3 * (N - 1) - 2 * J1 - J2
        Where:
        N = Number of links
        J1 = Number of 1-DOF joints (pins, sliders)
        J2 = Number of 2-DOF joints (gears, cams)
        """
        if links < 2:
            raise GeometricViolationError("A mechanism must have at least 2 links (including the ground frame).")
        if joints_1_dof < 0 or joints_2_dof < 0:
            raise GeometricViolationError("Number of joints cannot be negative.")

        mobility = (3 * (links - 1)) - (2 * joints_1_dof) - joints_2_dof
        return mobility

    @staticmethod
    def calculate_natural_frequency(stiffness: float, mass: float) -> float:
        """
        Calculates the undamped natural frequency (omega_n) of a single degree of freedom (SDOF) system.
        omega_n = sqrt(k / m)
        Unit: Radians per second (rad/s)
        """
        if stiffness <= 0:
            raise PhysicalBoundaryError("System stiffness (k) must be a positive non-zero value.")
        if mass <= 0:
            raise PhysicalBoundaryError("System mass (m) must be greater than zero.")

        return math.sqrt(stiffness / mass)

    @staticmethod
    def calculate_damping_ratio(damping_coefficient: float, stiffness: float, mass: float) -> float:
        """
        Calculates the dimensionless damping ratio (zeta) of a vibrating mechanical system.
        Zeta = c / (2 * sqrt(k * m))
        Regimes:
        - zeta < 1: Underdamped (oscillatory)
        - zeta = 1: Critically damped (fastest return to equilibrium)
        - zeta > 1: Overdamped (no oscillation, slow return)
        """
        if stiffness <= 0 or mass <= 0:
            raise PhysicalBoundaryError("Stiffness and mass must be positive properties.")
        if damping_coefficient < 0:
            raise PhysicalBoundaryError("Damping coefficient (c) cannot be negative.")

        critical_damping = 2.0 * math.sqrt(stiffness * mass)
        return damping_coefficient / critical_damping
