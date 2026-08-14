"""
Mega Engineering Library - Materials Science Validation Suite
"""
import pytest
from englib.materials.polymers import PolymerEngineering

def test_polymer_heterogeneity_index():
    """Validates macromolecular dispersity chains indexing validation."""
    pdi = PolymerEngineering.calculate_polydispersity_index(200000.0, 100000.0)
    assert pdi == 2.0
