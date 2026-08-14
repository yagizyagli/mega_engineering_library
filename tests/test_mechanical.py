"""
Mega Engineering Library - Mechanical Engineering Validation Suite
Validates fluid dynamics, thermal sciences, and solid mechanics stress calculations.
"""

import pytest
from englib.mechanical.fluid_mechanics import FluidMechanics
from englib.mechanical.solid_mechanics import SolidMechanics
from englib.common.exceptions import GeometricViolationError

def test_reynolds_flow_regime():
    """Validates the dimensionless Reynolds number calculations."""
    # Standard profile input: velocity=2.0, diameter=0.05, viscosity=1e-5
    re = FluidMechanics.calculate_reynolds_number(2.0, 0.05, 1e-5)
    assert re == 10000.0  # Must match analytical textbook calculation

def test_axial_stress_limits():
    """Verifies material strength formulas under structural loads."""
    # Force = 5000 N, Area = 100 mm²
    stress = SolidMechanics.calculate_axial_stress(5000.0, 100.0)
    assert stress == 50.0
    
    # Negative or zero areas must trigger geometric violations
    with pytest.raises(GeometricViolationError):
        SolidMechanics.calculate_axial_stress(5000.0, 0.0)
