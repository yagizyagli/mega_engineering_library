"""
Metallurgical Engineering Core Suite - 100% Complete Production Build
Unified entry point for extractive pyrometallurgy slag basicity ratios,
and Avrami solid-state alloy phase transformation kinetics.
"""

from englib.metallurgical.pyrometallurgy import Pyrometallurgy
from englib.metallurgical.phase_diagrams import MetallurgicalPhaseDiagrams

__all__ = [
    "Pyrometallurgy",
    "MetallurgicalPhaseDiagrams"
]
