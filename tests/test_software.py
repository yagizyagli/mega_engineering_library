"""
Mega Engineering Library - Software Engineering Validation Suite
"""
import pytest
from englib.software.complexity_metrics import ComplexityMetrics

def test_mccabe_cyclomatic_complexity():
    """Validates control flow graph logic branch risk boundaries."""
    m = ComplexityMetrics.calculate_mccabe_cyclomatic_complexity(15, 10, 1)
    assert m == 7
