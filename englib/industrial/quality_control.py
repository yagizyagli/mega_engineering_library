"""
Mega Engineering Library - Industrial Engineering & Operations Research: Quality Control Module
Handles statistical process control boundaries, defect variances, and manufacturing tolerances.
Validated against standard Six Sigma and engineering quality manuals (e.g., Montgomery).
"""

import math
from typing import List
from englib.common.exceptions import PhysicalBoundaryError

class QualityControl:

    @staticmethod
    def calculate_process_capability_index_cp(upper_spec_limit: float, lower_spec_limit: float, process_standard_deviation: float) -> float:
        """
        Calculates the short-term process capability index (Cp) to measure a manufacturing line's ability to produce within tolerance.
        Cp = (USL - LSL) / (6 * sigma)
        Generally, a Cp >= 1.33 is an industry standard benchmark.
        """
        if process_standard_deviation <= 0:
            raise PhysicalBoundaryError("Process variation standard deviation (sigma) must be positive and non-zero.")
        if upper_spec_limit <= lower_spec_limit:
            raise ValueError("Upper specification limit (USL) must be greater than the lower specification limit (LSL).")

        return (upper_spec_limit - lower_spec_limit) / (6.0 * process_standard_deviation)
