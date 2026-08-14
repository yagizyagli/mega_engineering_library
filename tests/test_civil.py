"""
Mega Engineering Library - Civil Engineering Structural Validation Suite
Verifies rigid-body equilibrium states and reinforced concrete strength block metrics.
"""

import pytest
from englib.civil.statics import CivilStatics
from englib.civil.concrete_design import ConcreteDesign

def test_simply_supported_beam_reactions():
    """Validates reaction forces for beams under single point loads."""
    # Beam length = 10m, Load = 100kN placed exactly at mid-span (5m)
    ry1, ry2 = CivilStatics.solve_simply_supported_beam_reactions(10.0, 100.0, 5.0)
    assert ry1 == 50.0
    assert ry2 == 50.0

def test_concrete_reinforcement_ratio():
    """Validates section steel reinforcement density indexes."""
    # Rebar Area = 400 mm², Width = 200 mm, Depth = 400 mm
    rho = ConcreteDesign.calculate_reinforcement_ratio(400.0, 200.0, 400.0)
    assert rho == 0.005
