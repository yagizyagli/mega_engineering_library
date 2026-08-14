"""
Electrical & Electronics Engineering Core Suite - 100% Complete Production Build
Unified entry point for circuit analysis, digital signal processing (DSP), electric power systems,
electromagnetic wave dynamics, semiconductor microelectronics, and classical control theory.
"""

from englib.electrical.circuit_analysis import CircuitAnalysis
from englib.electrical.dsp import DigitalSignalProcessing
from englib.electrical.power_systems import PowerSystems
from englib.electrical.electromagnetics import Electromagnetics
from englib.electrical.microelectronics import Microelectronics
from englib.electrical.control_systems import ControlSystems

__all__ = [
    "CircuitAnalysis",
    "DigitalSignalProcessing",
    "PowerSystems",
    "Electromagnetics",
    "Microelectronics",
    "ControlSystems"
]
