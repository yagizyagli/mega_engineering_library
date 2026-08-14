"""
Mega Engineering Library - Textile Engineering Validation Suite
"""
import pytest
from englib.textile.yarn_mechanics import YarnMechanics

def test_yarn_twist_factor_tex():
    """Verifies structural yarn layout density multi-variable twist metrics."""
    k = YarnMechanics.calculate_yarn_twist_factor_tex(50.0, 16.0)
    assert k == 200.0
