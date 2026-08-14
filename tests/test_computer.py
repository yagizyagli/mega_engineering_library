"""
Mega Engineering Library - Computer Engineering Validation Suite
"""
import pytest
from englib.computer.computer_architecture import ComputerArchitecture

def test_amdahl_parallel_speedup():
    """Verifies architectural scaling performance speedup limits."""
    speedup = ComputerArchitecture.calculate_amdahl_speedup(0.5, 2.0)
    assert speedup == 1.3333333333333333
