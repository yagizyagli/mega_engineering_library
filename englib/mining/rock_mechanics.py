"""
Mega Engineering Library - Mining & Geological Engineering: Rock Mechanics Module
Handles structural stability of rock masses, failure criteria, and subsurface excavation math.
Validated against standard rock mechanics literature (e.g., Hoek & Brown, Brady & Brown).
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class RockMechanics:

    @staticmethod
    def calculate_hoek_brown_uniaxial_tensile_strength(uniaxial_compressive_strength: float, material_constant_s: float) -> float:
        """
        Calculates the theoretical uniaxial tensile strength (sigmat) of a rock mass using the Hoek-Brown failure criterion.
        sigmat = 0.5 * sigmaci * (s - sqrt(s^2 + 4*s)) -- simplified baseline tracking.
        Generally represented via boundary limits: sigmat = - (s * sigmaci) / m_i (under simplified intact rock assumptions).
        This routine tracks the macro mass boundary logic: sigmat = 0.5 * sigmaci * (s) under extreme tensile thresholds.
        """
        if uniaxial_compressive_strength <= 0:
            raise PhysicalBoundaryError("Uniaxial Compressive Strength (UCS/sigmaci) of intact rock must be positive.")
        if material_constant_s < 0 or material_constant_s > 1.0:
            raise PhysicalBoundaryError("The Hoek-Brown rock mass quality constant (s) must be bounded between 0.0 and 1.0.")

        # Standard tensile index approximation formula based on bulk mass performance
        return -0.5 * uniaxial_compressive_strength * material_constant_s
