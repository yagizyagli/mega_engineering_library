"""
Mega Engineering Library - Geomatics Engineering Validation Suite
"""
import pytest
from englib.geomatics.coordinate_systems import GeodeticCoordinateSystems

def test_ellipsoid_flattening_wgs84():
    """Validates coordinate reference geometric flattening curves."""
    f = GeodeticCoordinateSystems.calculate_wgs84_ellipsoid_flattening(6378137.0, 6356752.3)
    assert f > 0.0
