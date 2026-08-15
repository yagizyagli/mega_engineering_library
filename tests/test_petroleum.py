"""
Mega Engineering Library - Petroleum Engineering Validation Suite
"""
import pytest
from englib.petroleum.production import PetroleumProduction

def test_vogel_inflow_performance():
    """Validates oil deliverability performance nodal curves."""
    q = PetroleumProduction.calculate_vogel_inflow_performance(1000.0, 1500.0, 2000.0)
    assert q == pytest.approx(400.0)
