"""
Mega Engineering Library - Nuclear Engineering: Radiation Shielding Module
Handles gamma and neutron radiation attenuation, absorption barriers, and shielding dimensions.
Validated against standard radiation protection guidelines.
"""

import math
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class RadiationShielding:

    @staticmethod
    def calculate_radiation_attenuation(initial_dose_rate: float, linear_attenuation_coeff_per_cm: float, shield_thickness_cm: float) -> float:
        """
        Calculates the transmitted radiation dose rate (I) behind a protective shielding barrier.
        I = I0 * exp(-mu * x)
        """
        if initial_dose_rate <= 0:
            raise PhysicalBoundaryError("Initial unprotected radiation source dose rate (I0) must be positive.")
        if linear_attenuation_coeff_per_cm < 0:
            raise PhysicalBoundaryError("Shield material attenuation attenuation coefficient (mu) cannot be negative.")
        if shield_thickness_cm < 0:
            raise GeometricViolationError("Shield barrier physical thickness cannot be negative.")

        return initial_dose_rate * math.exp(-linear_attenuation_coeff_per_cm * shield_thickness_cm)
