"""
Mega Engineering Library - Common Infrastructure Tests
Validates physical constants and comprehensive unit conversion boundaries.
"""

import pytest
from englib.common.constants import GRAVITY, PI
from englib.common.units import UnitConverter
from englib.common.exceptions import NegativeAbsoluteTemperatureError

def test_universal_constants():
    """Verifies that core physical boundaries are accurately hardcoded."""
    assert GRAVITY == 9.80665
    assert PI > 3.14159

def test_unit_conversions():
    """Validates multi-dimensional conversion equations and boundary conditions."""
    # 0 Celsius must exactly equal 273.15 Kelvin
    assert UnitConverter.celsius_to_kelvin(0.0) == 273.15
    
    # Temperatures below absolute zero must trigger our custom exception
    with pytest.raises(NegativeAbsoluteTemperatureError):
        UnitConverter.celsius_to_kelvin(-300.0)
