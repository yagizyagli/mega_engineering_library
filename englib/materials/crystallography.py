"""
Mega Engineering Library - Materials Science & Engineering: Crystallography Module
Handles crystal lattice systems, atomic planar spacing, and X-ray diffraction criteria.
Validated against standard materials science literature (e.g., Callister's Materials Science and Engineering).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class Crystallography:

    @staticmethod
    def calculate_bragg_interplanar_spacing(wavelength_meters: float, diffraction_angle_degrees: float, reflection_order: int = 1) -> float:
        """
        Calculates the interplanar spacing (d) between atomic planes using Bragg's Law.
        n * lambda = 2 * d * sin(theta) -> d = (n * lambda) / (2 * sin(theta))
        Unit: Meters (m)
        """
        if wavelength_meters <= 0:
            raise PhysicalBoundaryError("X-Ray source wavelength must be a positive non-zero value.")
        if reflection_order <= 0:
            raise PhysicalBoundaryError("The order of reflection (n) must be a positive integer.")
        if diffraction_angle_degrees <= 0.0 or diffraction_angle_degrees >= 180.0:
            raise GeometricViolationError("Diffraction angle must be within realistic physical boundaries (0 to 180 degrees).")

        # Bragg equation uses theta, which is half of the experimental 2-theta diffraction angle
        theta_radians = math.radians(diffraction_angle_degrees / 2.0)
        sin_theta = math.sin(theta_radians)

        if sin_theta == 0:
            raise ZeroDivisionError("Diffraction sine component yielded a zero evaluation matrix.")

        return (reflection_order * wavelength_meters) / (2.0 * sin_theta)
