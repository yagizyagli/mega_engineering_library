"""
Mega Engineering Library - Marine Engineering Validation Suite
"""
import pytest
from englib.marine.hydrostatics import MarineHydrostatics

def test_metacentric_stability():
    """Verifies ship capsize risk center parameters calculation."""
    gm = MarineHydrostatics.calculate_metacentric_height(3.0, 2.0, 4.0)
    assert gm == 1.0
