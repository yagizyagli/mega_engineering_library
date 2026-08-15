"""
Mega Engineering Library - Mining Engineering Validation Suite
"""
import pytest
from englib.mining.blasting import BlastingEngineering

def test_explosive_detonation_pressure():
    """Validates shock wave pressure outputs for commercial blasting."""
    pressure = BlastingEngineering.calculate_detonation_pressure(1.2, 4000.0)
    assert pressure == 4.8
