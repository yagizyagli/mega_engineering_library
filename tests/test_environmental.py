"""
Mega Engineering Library - Environmental Engineering Validation Suite
"""
import pytest
from englib.environmental.air_dispersion import AirDispersion

def test_gaussian_plume_dispersion():
    """Verifies factory emission atmospheric concentration calculations."""
    conc = AirDispersion.calculate_gaussian_plume_centerline_concentration(10.0, 5.0, 20.0, 10.0, 0.0)
    assert conc > 0.0
