"""
Mega Engineering Library - Biomedical Engineering: Medical Imaging Module
Handles tissue attenuation, ultrasound acoustic impedance, and imaging signal thresholds.
Validated against standard medical physics literature (e.g., Bushberg's The Essential Physics of Medical Imaging).
"""

import math
from englib.common.exceptions import PhysicalBoundaryError

class MedicalImaging:

    @staticmethod
    def calculate_xray_attenuation(initial_intensity: float, linear_attenuation_coeff: float, tissue_thickness_cm: float) -> float:
        """
        Calculates the transmitted X-Ray intensity (I) through a human tissue layer using the Beer-Lambert Law.
        I = I0 * exp(-mu * x)
        """
        if initial_intensity <= 0:
            raise PhysicalBoundaryError("Initial X-Ray beam intensity (I0) must be a positive non-zero value.")
        if linear_attenuation_coeff < 0:
            raise PhysicalBoundaryError("Tissue linear attenuation coefficient (mu) cannot be negative.")
        if tissue_thickness_cm < 0:
            raise PhysicalBoundaryError("Target tissue physical thickness context cannot be negative.")

        return initial_intensity * math.exp(-linear_attenuation_coeff * tissue_thickness_cm)
