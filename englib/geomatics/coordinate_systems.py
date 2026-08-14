"""
Mega Engineering Library - Geomatics Engineering: Coordinate Systems & Geodesy Module
Handles geodetic coordinate transformations, ellipsoid geometries, and WGS84 benchmarks.
Validated against standard geodesy and surveying literature (e.g., Vaníček & Krakiwsky).
"""

import math
from englib.common.exceptions import PhysicalBoundaryError, GeometricViolationError

class GeodeticCoordinateSystems:

    @staticmethod
    def calculate_wgs84_ellipsoid_flattening(semi_major_axis_a: float, semi_minor_axis_b: float) -> float:
        """
        Calculates the dimensionless flattening factor (f) of a planetary reference ellipsoid.
        f = (a - b) / a
        For Earth WGS84 standard reference: a = 6378137.0 m, b ~ 6356752.3142 m
        """
        if semi_major_axis_a <= 0 or semi_minor_axis_b <= 0:
            raise GeometricViolationError("Ellipsoid axis dimensions must be positive non-zero parameters.")
        if semi_major_axis_a <= semi_minor_axis_b:
            raise PhysicalBoundaryError("Physically impossible profile: Semi-major axis (a) must be greater than semi-minor axis (b).")

        return (semi_major_axis_a - semi_minor_axis_b) / semi_major_axis_a

    @staticmethod
    def convert_geodetic_to_ecef(latitude_degrees: float, longitude_degrees: float, height_meters: float, semi_major_axis_a: float = 6378137.0, flattening: float = 1.0/298.257223563) -> tuple[float, float, float]:
        """
        Converts Geodetic coordinates (Latitude, Longitude, Height) to Earth-Centered, Earth-Fixed (ECEF) Cartesian coordinates (X, Y, Z).
        Uses standard ellipsoidal coordinate transformation principles.
        """
        if latitude_degrees < -90.0 or latitude_degrees > 90.0:
            raise PhysicalBoundaryError("Latitude coordinates must fall strictly within the range of [-90, 90] degrees.")
        if longitude_degrees < -180.0 or longitude_degrees > 180.0:
            raise PhysicalBoundaryError("Longitude coordinates must fall strictly within the range of [-180, 180] degrees.")

        # Convert angles to radians
        lat_rad = math.radians(latitude_degrees)
        lon_rad = math.radians(longitude_degrees)

        # Compute first eccentricity squared (e^2)
        e_squared = (2.0 * flattening) - (flattening ** 2)

        # Compute radius of curvature in the prime vertical (N)
        sin_lat = math.sin(lat_rad)
        n_radius = semi_major_axis_a / math.sqrt(1.0 - (e_squared * (sin_lat ** 2)))

        # Compute ECEF Cartesian Coordinates
        cos_lat = math.cos(lat_rad)
        x = (n_radius + height_meters) * cos_lat * math.cos(lon_rad)
        y = (n_radius + height_meters) * cos_lat * math.sin(lon_rad)
        z = ((n_radius * (1.0 - e_squared)) + height_meters) * sin_lat

        return x, y, z
