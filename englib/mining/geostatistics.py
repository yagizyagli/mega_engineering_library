"""
Mega Engineering Library - Mining & Geological Engineering: Geostatistics Module
Handles spatial ore reserve estimation, spatial data weights, and resource tracking.
Validated against standard geostatistical literature (e.g., Isaaks & Srivastava).
"""

from typing import List
from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class Geostatistics:

    @staticmethod
    def calculate_inverse_distance_weighting_2d(sample_grades: List[float], distances: List[float], power_exponent: float = 2.0) -> float:
        """
        Estimates the unknown block grade at a specific grid node using Inverse Distance Weighting (IDW).
        Grade = sum(Grade_i / d_i^p) / sum(1 / d_i^p)
        """
        if not sample_grades or not distances:
            raise ValueError("Sample grade and distance input lists cannot be empty.")
        if len(sample_grades) != len(distances):
            raise GeometricViolationError("Mismatched datasets: Array lengths for grades and spatial distances must match.")
        if power_exponent <= 0:
            raise PhysicalBoundaryError("IDW spatial tracking power exponent weight must be positive.")

        numerator_sum = 0.0
        denominator_sum = 0.0

        for grade, dist in zip(sample_grades, distances):
            if dist <= 0:
                # If a drill sample sits exactly on the estimation node, its distance is zero.
                # Returns the exact grade directly to avoid division by zero.
                return grade
                
            weight = 1.0 / (dist ** power_exponent)
            numerator_sum += grade * weight
            denominator_sum += weight

        return numerator_sum / denominator_sum
