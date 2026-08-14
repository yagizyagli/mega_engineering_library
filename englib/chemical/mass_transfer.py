"""
Mega Engineering Library - Chemical Engineering: Mass Transfer Module
Handles molecular diffusion fluxes, binary mass transfer, and separation profiles.
Validated against standard transport phenomena literature (e.g., Bird, Stewart, & Lightfoot).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class MassTransfer:

    @staticmethod
    def calculate_fick_diffusion_flux(diffusion_coefficient: float, concentration_diff: float, distance_delta: float) -> float:
        """
        Calculates the steady-state molecular diffusion flux (JA) using Fick's First Law.
        J = -D * (dC / dx) -> Magnified format: J = D * (C1 - C2) / delta_x
        Unit: mol/(m²·s)
        """
        if distance_delta <= 0:
            raise GeometricViolationError("Diffusion path length thickness (delta_x) must be greater than zero.")
        if diffusion_coefficient <= 0:
            raise PhysicalBoundaryError("Mass diffusivity/diffusion coefficient (D) must be a positive physical property.")

        return (diffusion_coefficient * concentration_diff) / distance_delta
