"""
Mega Engineering Library - Electrical Engineering Validation Suite
Verifies circuit topologies, nodal Ohm laws, and Nyquist signal frequencies.
"""

import pytest
from englib.electrical.circuit_analysis import CircuitAnalysis
from englib.electrical.dsp import DigitalSignalProcessing

def test_ohm_law_solver():
    """Validates parameter configurations across standard active electric nets."""
    # Solves for Voltage given Current = 2A and Resistance = 10 Ohms
    v = CircuitAnalysis.calculate_ohm_law(current=2.0, resistance=10.0)
    assert v == 20.0

def test_nyquist_sampling_rate():
    """Verifies aliasing frequency thresholds for analog conversions."""
    # Max signal frequency component = 44100 Hz (Audio CD benchmark standard)
    rate = DigitalSignalProcessing.calculate_nyquist_rate(44100.0)
    assert rate == 88200.0
