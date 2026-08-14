"""
Mega Engineering Library - Geomatics Engineering: Photogrammetry & Remote Sensing Module
Handles focal length calculations, image scale, and collinearity camera projections.
Validated against standard photogrammetry literature (e.g., Wolf & Dewitt's Elements of Photogrammetry).
"""

from englib.common.exceptions import GeometricViolationError, PhysicalBoundaryError

class Photogrammetry:

    @staticmethod
    def calculate_photogrammetric_scale(focal_length_mm: float, flying_height_above_ground_meters: float) -> float:
        """
        Calculates the representative fraction scale (S) of a vertical aerial photograph profile.
        S = focal_length / flying_height (after balancing standard units internally)
        Returns the scale denominator (e.g., 5000 means a scale of 1:5000).
        """
        if focal_length_mm <= 0:
            raise PhysicalBoundaryError("Camera focal length must be a positive non-zero physical property.")
        if flying_height_above_ground_meters <= 0:
            raise GeometricViolationError("Aircraft or drone flying height above the terrain datum must be positive.")

        # Convert focal length from mm to meters: focal_length_mm / 1000
        focal_length_meters = focal_length_mm / 1000.0
        scale_denominator = flying_height_above_ground_meters / focal_length_meters
        return scale_denominator
