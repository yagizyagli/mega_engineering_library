"""
Mega Engineering Library - Software & Systems Engineering: Cost Estimation Module
Handles software project effort estimation, staffing metrics, and schedule planning models.
Validated against standard software engineering literature (e.g., Boehm's COCOMO II Model).
"""

from englib.common.exceptions import PhysicalBoundaryError, GeometricViolationError

class SoftwareCostEstimation:

    @staticmethod
    def calculate_cocomo_effort_person_months(size_kloc: float, baseline_constant_a: float = 2.94, scale_exponent_b: float = 1.15) -> float:
        """
        Calculates the required development effort in Person-Months (PM) using the COCOMO II Post-Architecture Model.
        Effort = A * (Size)^B
        Where:
        size_kloc = Size of the software project in Thousands of Lines of Code (KLOC)
        baseline_constant_a = Nominal effort coefficient (defaults to COCOMO II standard 2.94)
        scale_exponent_b = Scale factor exponent reflecting project scaling economies (defaults to 1.15)
        Unit: Person-Months (PM)
        """
        if size_kloc <= 0:
            raise GeometricViolationError("Software source code project size (KLOC) must be a positive non-zero value.")
        if baseline_constant_a <= 0 or scale_exponent_b <= 0:
            raise PhysicalBoundaryError("COCOMO empirical calibration coefficients must be positive.")

        return baseline_constant_a * (size_kloc ** scale_exponent_b)
