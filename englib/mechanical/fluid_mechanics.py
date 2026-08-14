"""
Mega Engineering Library - Mechanical Engineering: Fluid Mechanics Module
Contains core computational formulas for fluid dynamics, pipe networks, and hydraulics.
Validated against standard academic literature (e.g., Munson, Young, and Okiishi).
"""

import math
from englib.common.constants import GRAVITY
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class FluidMechanics:

    @staticmethod
    def calculate_reynolds_number(velocity: float, diameter: float, kinematic_viscosity: float) -> float:
        """
        Calculates the dimensionless Reynolds Number (Re) to determine flow regime.
        Re = (Velocity * Diameter) / Kinematic Viscosity
        
        Flow regimes for pipe flow:
        - Re < 2300: Laminar flow
        - 2300 <= Re <= 4000: Transitional flow
        - Re > 4000: Turbulent flow
        """
        if diameter <= 0:
            raise GeometricViolationError("Pipe diameter must be greater than zero.")
        if kinematic_viscosity <= 0:
            raise PhysicalBoundaryError("Kinematic viscosity must be a positive non-zero value.")
        if velocity < 0:
            raise PhysicalBoundaryError("Velocity cannot be negative.")
            
        return (velocity * diameter) / kinematic_viscosity

    @staticmethod
    def calculate_pipe_friction_factor_laminar(reynolds_number: float) -> float:
        """
        Calculates the Darcy friction factor (f) for fully developed laminar pipe flow.
        Valid only for Reynolds Number < 2300.
        f = 64 / Re
        """
        if reynolds_number <= 0:
            raise PhysicalBoundaryError("Reynolds number must be greater than zero.")
            
        return 64.0 / reynolds_number

    @staticmethod
    def calculate_head_loss_darcy(friction_factor: float, length: float, diameter: float, velocity: float) -> float:
        """
        Calculates pressure/head loss (hf) in a pipe using the Darcy-Weisbach equation.
        hf = f * (L / D) * (V^2 / 2g)
        Returns the head loss in meters (m).
        """
        if diameter <= 0 or length <= 0:
            raise GeometricViolationError("Pipe dimensions (length and diameter) must be positive.")
        if friction_factor <= 0:
            raise PhysicalBoundaryError("Friction factor must be greater than zero.")
            
        velocity_head = (velocity ** 2) / (2.0 * GRAVITY)
        return friction_factor * (length / diameter) * velocity_head

    @staticmethod
    def verify_bernoulli_velocity(p1: float, p2: float, z1: float, z2: float, v1: float, density: float) -> float:
        """
        Calculates the unknown exit velocity (v2) using the frictionless Bernoulli Equation.
        Assumes steady, incompressible flow without losses.
        (P1 / rho*g) + (V1^2 / 2g) + Z1 = (P2 / rho*g) + (V2^2 / 2g) + Z2
        Returns velocity v2 in m/s.
        """
        if density <= 0:
            raise PhysicalBoundaryError("Fluid density must be greater than zero.")
            
        total_head_1 = (p1 / (density * GRAVITY)) + ((v1 ** 2) / (2.0 * GRAVITY)) + z1
        v2_head_component = total_head_1 - (p2 / (density * GRAVITY)) - z2
        
        if v2_head_component < 0:
            raise PhysicalBoundaryError("Physically impossible state: Energy balance results in negative kinetic energy.")
            
        return math.sqrt(v2_head_component * 2.0 * GRAVITY)
