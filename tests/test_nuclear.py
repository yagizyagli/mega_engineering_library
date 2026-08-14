"""
Mega Engineering Library - Nuclear Engineering Validation Suite
"""
import pytest
from englib.nuclear.reactor_physics import NuclearReactorPhysics

def test_reactor_six_factor_criticality():
    """Verifies fission chain multiplication reproduction checks."""
    k = NuclearReactorPhysics.calculate_six_factor_multiplication_factor(1.05, 0.95, 0.85, 1.02, 0.98, 0.98)
    assert k < 1.0
