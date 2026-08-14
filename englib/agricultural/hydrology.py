"""
Mega Engineering Library - Agricultural & Biosystems Engineering: Agricultural Hydrology Module
Handles peak surface runoff and open watershed drainage calculations.
Validated against standard hydrology and engineering principles (e.g., Schwab's Soil and Water Conservation Engineering).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class AgriculturalHydrology:

    @staticmethod
    def calculate_peak_runoff_rational(runoff_coefficient: float, rainfall_intensity_mm_hr: float, watershed_area_ha: float) -> float:
        """
        Calculates the peak runoff rate (Q) using the standard Rational Method.
        Q = (C * I * A) / 360
        Where:
        C = Dimensionless runoff coefficient (0.0 to 1.0)
        I = Rainfall intensity in mm/hr
        A = Watershed drainage area in hectares (ha)
        Returns the peak discharge in cubic meters per second (m³/s).
        """
        if runoff_coefficient < 0.0 or runoff_coefficient > 1.0:
            raise PhysicalBoundaryError("The runoff coefficient (C) must be a bounded fractional ratio between 0.0 and 1.0.")
        if rainfall_intensity_mm_hr <= 0:
            raise PhysicalBoundaryError("Rainfall intensity (I) must be a positive non-zero profile calculation.")
        if watershed_area_ha <= 0:
            raise GeometricViolationError("Watershed drainage surface area (A) must be greater than zero.")

        # Metric conversions coefficient: 1 / 360
        return (runoff_coefficient * rainfall_intensity_mm_hr * watershed_area_ha) / 360.0
